import os
from typing import Sequence
from fastapi import FastAPI, HTTPException

from sqlalchemy import select

from fastapi.middleware.cors import CORSMiddleware

from .dependencies import SessionDep
from .models import Staff, StaffPublic, Menu, MenuPublic


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

    stmt = select(Menu).where(Menu.location_id == location_id)
    return session.scalars(stmt).all()

