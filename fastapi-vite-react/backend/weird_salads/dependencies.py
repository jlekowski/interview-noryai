from functools import lru_cache
from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy import Engine
from sqlmodel import Session, create_engine

from .config import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()


@lru_cache
def get_engine(settings: Annotated[Settings, Depends(get_settings)]) -> Engine:
    return create_engine(settings.db_uri.unicode_string())


def get_session(engine: Annotated[Engine, Depends(get_engine)]) -> Generator[Session]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
