"""Create stock table

Revision ID: 698e3e3e0adf
Revises: d04827eec998
Create Date: 2025-06-12 12:41:50.064040

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '698e3e3e0adf'
down_revision: Union[str, None] = 'd04827eec998'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'stock',
        sa.Column('location_id', sa.Integer, nullable=False),
        sa.Column('ingredient_id', sa.Integer, nullable=False),
        sa.Column('quantity', sa.Numeric(10, 2), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("stock")
