"""Add is_verified column

Revision ID: 451f61f7f7cb
Revises: 5683123ff89a
Create Date: 2020-08-29 17:19:32.029529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '451f61f7f7cb'
down_revision = '5683123ff89a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_verified')
    # ### end Alembic commands ###
