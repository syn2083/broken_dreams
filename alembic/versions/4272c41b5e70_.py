"""empty message

Revision ID: 4272c41b5e70
Revises: 113b4f2ac013
Create Date: 2016-05-15 22:41:48.260353

"""

# revision identifiers, used by Alembic.
revision = '4272c41b5e70'
down_revision = '113b4f2ac013'
branch_labels = None
depends_on = None

from alembic import op
from alembic import context
import sqlalchemy as sa


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()

def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()

def schema_upgrades():
    """schema upgrade migrations go here."""
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('option',
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('version', sa.String(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('wizlock', sa.Boolean(), nullable=True),
    sa.Column('hotboot', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('date_created')
    )
    op.create_table('pulse',
    sa.Column('width', sa.Float(), nullable=False),
    sa.Column('violence', sa.Float(), nullable=True),
    sa.Column('river', sa.Float(), nullable=True),
    sa.Column('teleport', sa.Float(), nullable=True),
    sa.Column('nature', sa.Float(), nullable=True),
    sa.Column('mobile', sa.Float(), nullable=True),
    sa.Column('sound', sa.Float(), nullable=True),
    sa.Column('zone', sa.Float(), nullable=True),
    sa.Column('update', sa.Float(), nullable=True),
    sa.Column('variation', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('width')
    )
    ### end Alembic commands ###

def schema_downgrades():
    """schema downgrade migrations go here."""
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pulse')
    op.drop_table('option')
    ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
