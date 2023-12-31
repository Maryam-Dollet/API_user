"""remove phone number column from users

Revision ID: 5d6d00c125aa
Revises: a2d3ec42c43e
Create Date: 2023-09-04 21:04:33.623144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5d6d00c125aa"
down_revision: Union[str, None] = "a2d3ec42c43e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "phonenumber")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("phonenumber", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###
