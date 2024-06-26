"""add user role

Revision ID: 9d819808eb62
Revises: 259a5ef98533
Create Date: 2024-03-28 07:28:01.893272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d819808eb62'
down_revision: Union[str, None] = '259a5ef98533'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE role as ENUM('admin', 'moderator', 'user')")
    op.add_column('users', sa.Column('role', sa.Enum('admin', 'moderator', 'user', name='role'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    op.execute("DROP TYPE role")
    # ### end Alembic commands ###
