"""add foreign key to characters table

Revision ID: 652dd1ff6e93
Revises: 7f14247c0c23
Create Date: 2023-09-04 20:23:45.170676

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = "652dd1ff6e93"
down_revision: Union[str, None] = "7f14247c0c23"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("characters", sa.Column("user_id", UUID, nullable=False))
    op.create_foreign_key(
        "characters_users_fk",
        source_table="characters",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["user_id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("characters_users_fk", table_name="characters")
    op.drop_column("characters", "user_id")
    pass
