"""add foreign-key to posts table

Revision ID: 72bcddba6668
Revises: 513cf460e4fd
Create Date: 2022-06-07 19:18:16.594443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72bcddba6668'
down_revision = '513cf460e4fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
