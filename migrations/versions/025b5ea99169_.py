"""empty message

Revision ID: 025b5ea99169
Revises: a8ed6e4aacfd
Create Date: 2018-07-18 20:23:52.643417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '025b5ea99169'
down_revision = 'a8ed6e4aacfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messageboard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messageboard')
    # ### end Alembic commands ###
