"""empty message

Revision ID: c5ef5707e2e5
Revises: 6ee2237532bf
Create Date: 2016-10-01 13:25:26.414361

"""

# revision identifiers, used by Alembic.
revision = 'c5ef5707e2e5'
down_revision = '6ee2237532bf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('announcements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('announcements')
    ### end Alembic commands ###
