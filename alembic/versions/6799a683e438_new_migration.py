"""new migration

Revision ID: 6799a683e438
Revises: 775c6d6a166d
Create Date: 2025-01-03 12:43:58.169496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6799a683e438'
down_revision: Union[str, None] = '775c6d6a166d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
