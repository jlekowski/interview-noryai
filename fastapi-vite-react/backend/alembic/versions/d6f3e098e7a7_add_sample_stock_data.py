"""Add sample stock data

Revision ID: d6f3e098e7a7
Revises: 698e3e3e0adf
Create Date: 2025-06-12 13:32:27.018550

"""
import csv
import os
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd6f3e098e7a7'
down_revision: Union[str, None] = '698e3e3e0adf'
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
        table_name='stock',
        column_defs=[
            ('location_id', sa.Integer),
            ('ingredient_id', sa.Integer),
            ('quantity', sa.Numeric),
        ],
        csv_filename='stock_data.csv'
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
