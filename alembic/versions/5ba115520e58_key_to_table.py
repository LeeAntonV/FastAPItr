"""key_to_table

Revision ID: 5ba115520e58
Revises: 45b544f18c54
Create Date: 2023-04-13 21:01:22.874316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ba115520e58'
down_revision = '45b544f18c54'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Grade_Table', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('table_users_fk', source_table="Grade_Table", referent_table="Table", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass

def downgrade():
    op.drop_constraint("table_users_fk",table_name="Grade_Table")
    op.drop_column("Grade_Table","owner_id")
    pass
