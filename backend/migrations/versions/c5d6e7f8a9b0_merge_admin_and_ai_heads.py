"""Merge the administration and AI migration branches."""

from typing import Sequence, Union


revision: str = "c5d6e7f8a9b0"
down_revision: Union[str, Sequence[str], None] = (
    "a1b2c3d4e5f6",
    "b4edef72481a",
)
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass