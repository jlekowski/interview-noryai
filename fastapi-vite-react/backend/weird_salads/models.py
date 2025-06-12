from datetime import datetime

from decimal import Decimal
from sqlmodel import Field, SQLModel


class StaffBase(SQLModel):
    staff_id: int
    name: str
    location: int
    date_of_birth: datetime
    iban: str
    bic: str


class Staff(StaffBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class StaffPublic(StaffBase):
    id: int = Field(exclude=True)


class MenuBase(SQLModel):
    recipe_id: int
    name: str
    price: Decimal
    is_available: bool


class Menu(MenuBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class MenuPublic(MenuBase):
    id: int = Field(exclude=True)


class RecipeBase(SQLModel):
    recipe_id: int
    name: str
    quantity: Decimal
    ingredient_id: int


class Recipe(RecipeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class StockBase(SQLModel):
    location_id: int
    quantity: Decimal
    ingredient_id: int


class Stock(StockBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
