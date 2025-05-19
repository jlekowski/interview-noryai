"""Create staff table

Revision ID: 50fc5d40310d
Revises:
Create Date: 2025-05-16 15:16:52.931204

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "50fc5d40310d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "staff",
        sa.Column("staff_id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("location", sa.Integer(), nullable=False),
        sa.Column("date_of_birth", sa.DateTime(), nullable=False),
        sa.Column("iban", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("bic", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("staff")
