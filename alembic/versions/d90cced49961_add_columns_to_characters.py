"""add columns to characters

Revision ID: d90cced49961
Revises: 652dd1ff6e93
Create Date: 2023-09-04 20:30:07.982975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d90cced49961"
down_revision: Union[str, None] = "652dd1ff6e93"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("characters", sa.Column("age", sa.Integer, nullable=True))
    op.add_column(
        "characters", sa.Column("affiliation", sa.String, server_default="Not Provided")
    )
    op.add_column(
        "characters",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("characters", "age")
    op.drop_column("characters", "affiliation")
    op.drop_column("characters", "created_at")
    pass
