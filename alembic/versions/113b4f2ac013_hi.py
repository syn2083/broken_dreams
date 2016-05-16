"""hi

Revision ID: 113b4f2ac013
Revises: 2115e3307d8d
Create Date: 2016-05-15 22:32:50.158011

"""

# revision identifiers, used by Alembic.
revision = '113b4f2ac013'
down_revision = '2115e3307d8d'
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
    pass

def schema_downgrades():
    """schema downgrade migrations go here."""
    pass

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
