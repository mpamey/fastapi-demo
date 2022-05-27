"""create posts table

Revision ID: 729000a50b17
Revises: 
Create Date: 2022-05-27 12:19:01.126793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '729000a50b17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )



def downgrade():
    op.drop_table(table_name='posts')

