# Weird Salads FastAPI starter

Weird Salads starter with a [FastAPI](https://fastapi.tiangolo.com/) backend.

PostgreSQL is used for the database and [SQLAlchemy](https://www.sqlalchemy.org/) is used under the hood for SQL queries.

[SQLModel](https://sqlmodel.tiangolo.com/) is used for FastAPI and SQLAlchemy integration. See the [FastAPI SQL guide](https://fastapi.tiangolo.com/tutorial/sql-databases/) for more details.

[uv](docs.astral.sh/uv) is used for dependency management, and to run the code.

## Running commands with uv

Most python commands will work with a `uv run` prefix:
```sh
# Ensuring dependencies are installed
uv sync

# Running python
uv run python

# Starting FastAPI
uv run fastapi dev weird_salads/app.py

# Running migrations
uv run alembic upgrade head

# Creating migrations
uv run alembic revision --autogenerate --message "My migration"
```

## Notes

Initially configured using:
```sh
uv init
uv add fastapi[standard] alembic psycopg[binary,pool] pydantic-settings sqlalchemy sqlmodel
uv add --dev ruff mypy
```
