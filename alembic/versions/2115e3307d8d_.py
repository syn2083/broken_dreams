"""empty message

Revision ID: 2115e3307d8d
Revises: e1d9e941db75
Create Date: 2016-05-15 22:24:58.960758

"""

# revision identifiers, used by Alembic.
revision = '2115e3307d8d'
down_revision = 'e1d9e941db75'
branch_labels = None
depends_on = None

from alembic import op
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
    op.drop_table('option')
    ### end Alembic commands ###

def schema_downgrades():
    """schema downgrade migrations go here."""
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('option',
    sa.Column('date_created', sa.DATETIME(), nullable=False),
    sa.Column('version', sa.VARCHAR(), nullable=True),
    sa.Column('port', sa.INTEGER(), nullable=True),
    sa.Column('wizlock', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('date_created')
    )
    ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
