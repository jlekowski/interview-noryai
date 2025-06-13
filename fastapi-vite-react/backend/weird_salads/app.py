import os
from typing import Sequence
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from sqlalchemy import select, text, case, update, and_

from fastapi.middleware.cors import CORSMiddleware

from .dependencies import SessionDep
from .models import Staff, StaffPublic, Menu, MenuPublic, Recipe, Stock


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConsumeRecipeRequest(BaseModel):
    staff_id: int

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/staff/", response_model=list[StaffPublic])
def list_staff(session: SessionDep) -> Sequence[Staff]:
    location_id = os.getenv("APP_LOCATION_ID")
    if location_id is None:
        raise HTTPException(status_code=500, detail="APP_LOCATION_ID not set")

    try:
        location_id = int(location_id)
    except ValueError:
        raise HTTPException(status_code=500, detail="APP_LOCATION_ID must be an integer")

    stmt = select(Staff).where(Staff.location == location_id)
    return session.scalars(stmt).all()


@app.get("/menu/", response_model=list[MenuPublic])
def list_menu(session: SessionDep) -> Sequence[Menu]:
    location_id = os.getenv("APP_LOCATION_ID")
    if location_id is None:
        raise HTTPException(status_code=500, detail="APP_LOCATION_ID not set")

    try:
        location_id = int(location_id)
    except ValueError:
        raise HTTPException(status_code=500, detail="APP_LOCATION_ID must be an integer")

    # Problem solved: showing item availability (but not showing the number of the items available)
    sql = text("""
        SELECT
            m.id,
            r.recipe_id,
            r.name,
            m.price,
            bool_and(COALESCE(s.quantity, 0) >= r.quantity) AS is_available
        FROM menu m
        JOIN recipe r ON m.recipe_id = r.recipe_id
        LEFT JOIN stock s ON r.ingredient_id = s.ingredient_id
        WHERE m.location_id = :location_id
        GROUP BY m.id, r.recipe_id, m.price, r.name
    """)

    result = session.execute(sql, {"location_id": location_id})
    rows = result.mappings().all()

    return rows

@app.post("/recipe/{recipe_id}/consume")
def consume_stock(recipe_id: int, req: ConsumeRecipeRequest, session: SessionDep):
    # ignoring for the time being, but would be used to log who made the change
    staff_id = req.staff_id
    # validate that the recipe "belongs" to the location

    location_id = int(os.getenv("APP_LOCATION_ID"))
    stmt = select(Recipe).where(Recipe.recipe_id == recipe_id)
    recipe_ingredients = session.scalars(stmt).all()

    if not recipe_ingredients:
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Problem solved: it was interesting to find a way to update multiple ingredients' stock in one UPDATE query
    # Prepare WHEN conditions for the CASE statement
    when_conditions = [(r.ingredient_id, r.quantity) for r in recipe_ingredients]

    # Build CASE expression with Stock.ingredient_id
    case_stmt = case(
        {ingredient_id: quantity for ingredient_id, quantity in when_conditions},
        value=Stock.ingredient_id,
        else_=0
    )

    # Generate SQLAlchemy update statement
    update_stmt = (
        update(Stock)
        .where(
            and_(
                Stock.ingredient_id.in_([r.ingredient_id for r in recipe_ingredients]),
                Stock.location_id == location_id
            )
        )
        .values(quantity=Stock.quantity - case_stmt)
    )

    session.execute(update_stmt)
    session.commit()

    """
    e.g.
    UPDATE stock
    SET quantity = quantity - CASE ingredient_id
                                  WHEN 15 THEN 1
                                  WHEN 2 THEN 3
                                  ELSE 0
                              END
    WHERE location_id = 1;
    """

    return staff_id
