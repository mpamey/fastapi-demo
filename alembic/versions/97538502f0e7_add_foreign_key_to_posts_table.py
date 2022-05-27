"""add foreign key to posts table


Revision ID: 97538502f0e7
Revises: 1756e14644d7
Create Date: 2022-05-27 13:26:59.047330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97538502f0e7'
down_revision = '1756e14644d7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(constraint_name='posts_users_fk', source_table='posts', referent_table="users",
                          local_cols=['user_id'], remote_cols=['user_id'], ondelete="CASCADE")

def downgrade():
    op.drop_constraint('posts_users_fk', 'posts')
    op.drop_column('posts', 'user_id')
