"""add user table

Revision ID: 1756e14644d7
Revises: 854ade565f86
Create Date: 2022-05-27 13:17:44.836023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1756e14644d7'
down_revision = '854ade565f86'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('user_id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.UniqueConstraint('email')
                    )


def downgrade():
    op.drop_table('users')
