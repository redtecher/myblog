"""empty message

Revision ID: d0ed60886096
Revises: 025b5ea99169
Create Date: 2018-08-17 22:54:06.972472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0ed60886096'
down_revision = '025b5ea99169'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('private', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'private')
    # ### end Alembic commands ###
