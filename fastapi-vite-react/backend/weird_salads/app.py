from typing import Sequence
from fastapi import FastAPI

from sqlalchemy import select

from fastapi.middleware.cors import CORSMiddleware

from .dependencies import SessionDep
from .models import Staff, StaffPublic


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
    return session.scalars(select(Staff)).all()
