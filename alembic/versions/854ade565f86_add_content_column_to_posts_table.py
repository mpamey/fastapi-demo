"""add content column to posts table

Revision ID: 854ade565f86
Revises: 729000a50b17
Create Date: 2022-05-27 13:13:24.497037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '854ade565f86'
down_revision = '729000a50b17'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
