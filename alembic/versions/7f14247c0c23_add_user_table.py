"""add user table

Revision ID: 7f14247c0c23
Revises: 5847d1ce23b5
Create Date: 2023-09-04 19:30:38.655109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = "7f14247c0c23"
down_revision: Union[str, None] = "5847d1ce23b5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "user_id", UUID(as_uuid=True), server_default=sa.text("uuid_generate_v1()")
        ),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("password", sa.String, nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
