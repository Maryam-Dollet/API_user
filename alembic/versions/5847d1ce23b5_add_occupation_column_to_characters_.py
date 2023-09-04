"""add occupation column to characters table

Revision ID: 5847d1ce23b5
Revises: b0af5a2060c3
Create Date: 2023-09-04 19:21:03.911327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5847d1ce23b5"
down_revision: Union[str, None] = "b0af5a2060c3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("characters", sa.Column("occupation", sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("characters", "occupation")
    pass
