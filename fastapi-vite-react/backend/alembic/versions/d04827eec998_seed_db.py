"""Seed DB

Revision ID: d04827eec998
Revises: 826078be338e
Create Date: 2025-06-11 13:15:22.804220

"""
import csv
import os
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd04827eec998'
down_revision: Union[str, None] = '826078be338e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def seed_from_csv(table_name, column_defs, csv_filename):
    """
    Seed a table with data from a CSV file.

    :param table_name: name of the table to insert into
    :param column_defs: list of (column_name, sqlalchemy_type) tuples
    :param csv_filename: relative path to CSV file (relative to this script)
    """
    # Build SQLAlchemy table object
    tbl = sa.sql.table(
        table_name,
        *[sa.sql.column(col_name, col_type) for col_name, col_type in column_defs]
    )

    # Resolve path relative to this script file
    script_dir = os.path.dirname(__file__)
    csv_path = os.path.join(script_dir, csv_filename)

    # Read CSV and insert
    connection = op.get_bind()
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            cleaned_row = {
                key: (value if value.strip() != '' else None)
                for key, value in row.items()
            }
            rows.append(cleaned_row)

        if rows:
            connection.execute(tbl.insert(), rows)


def upgrade() -> None:
    """Upgrade schema."""
    seed_from_csv(
        table_name='ingredient',
        column_defs=[
            ('ingredient_id', sa.Integer),
            ('name', sa.String),
            ('unit', sa.String),
            ('cost', sa.Numeric)
        ],
        csv_filename='ingredient_data.csv'
    )

    seed_from_csv(
        table_name='location',
        column_defs=[
            ('location_id', sa.Integer),
            ('name', sa.String),
            ('address', sa.String)
        ],
        csv_filename='location_data.csv'
    )

    seed_from_csv(
        table_name='recipe',
        column_defs=[
            ('recipe_id', sa.Integer),
            ('name', sa.String),
            ('quantity', sa.Numeric),
            ('ingredient_id', sa.Integer)
        ],
        csv_filename='recipe_data.csv'
    )

    seed_from_csv(
        table_name='modifier',
        column_defs=[
            ('modifier_id', sa.Integer),
            ('name', sa.String),
            ('option', sa.String),
            ('price', sa.Numeric)
        ],
        csv_filename='modifier_data.csv'
    )

    seed_from_csv(
        table_name='menu',
        column_defs=[
            ('recipe_id', sa.Integer),
            ('location_id', sa.Integer),
            ('price', sa.Numeric),
            ('modifiers', sa.Integer)
        ],
        csv_filename='menu_data.csv'
    )

    seed_from_csv(
        table_name='staff',
        column_defs=[
            ('staff_id', sa.Integer),
            ('name', sa.String),
            ('date_of_birth', sa.Date),
            # ('role', sa.String),
            ('iban', sa.String),
            ('bic', sa.String),
            ('location', sa.Integer)
        ],
        csv_filename='staff_data.csv'
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
