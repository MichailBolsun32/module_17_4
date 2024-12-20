"""empty message

Revision ID: 506a28eec2bf
Revises: ba20be224825
Create Date: 2024-12-20 02:51:43.135596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '506a28eec2bf'
down_revision: Union[str, None] = 'ba20be224825'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
