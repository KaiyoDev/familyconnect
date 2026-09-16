"""Create the base FamilyConnect schema."""

from typing import Sequence, Union

from alembic import op

from app.infrastructure.databases.base import Base
from app.infrastructure.models import community, directory, event, genealogy, heritage, user, types  # noqa: F401

revision: str = "78ad87157e85"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

_EXCLUDED_TABLES = {
    "audit_logs",
    "notifications",
    "system_configs",
    "ai_conversations",
    "ai_messages",
}


def _base_tables():
    return [
        table
        for table in Base.metadata.sorted_tables
        if table.name not in _EXCLUDED_TABLES
    ]


def upgrade() -> None:
    bind = op.get_bind()
    Base.metadata.create_all(bind=bind, tables=_base_tables())


def downgrade() -> None:
    bind = op.get_bind()
    Base.metadata.drop_all(bind=bind, tables=list(reversed(_base_tables())))
