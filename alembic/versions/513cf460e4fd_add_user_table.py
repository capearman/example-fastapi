"""add user table

Revision ID: 513cf460e4fd
Revises: 5063c353d68f
Create Date: 2022-06-07 18:42:38.458509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '513cf460e4fd'
down_revision = '5063c353d68f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')

    )


def downgrade() -> None:
    op.drop_table('users')
