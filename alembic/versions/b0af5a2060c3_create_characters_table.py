"""create characters table

Revision ID: b0af5a2060c3
Revises: 
Create Date: 2023-09-04 19:09:35.689385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = "b0af5a2060c3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "characters",
        sa.Column(
            "character_id",
            UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            server_default=sa.text("uuid_generate_v1()"),
        ),
        sa.Column("name", sa.String, nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("characters")
    pass
