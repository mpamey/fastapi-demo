"""add last few columns to posts table

Revision ID: 6a9740eb0297
Revises: 97538502f0e7
Create Date: 2022-05-27 13:32:15.047179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a9740eb0297'
down_revision = '97538502f0e7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),
                  )
    op.add_column('posts', sa.Column('rating', sa.Integer(), nullable=True),
                  )
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                  )


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'rating')
    op.drop_column('posts', 'created_at')
