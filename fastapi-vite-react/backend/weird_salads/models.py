from datetime import datetime

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
