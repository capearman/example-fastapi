"""add content_column to posts table

Revision ID: 5063c353d68f
Revises: 51f581a60719
Create Date: 2022-06-07 18:31:59.634819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5063c353d68f'
down_revision = '51f581a60719'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))



def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
