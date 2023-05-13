"""create table

Revision ID: 45b544f18c54
Revises: 
Create Date: 2023-04-13 16:54:12.571256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45b544f18c54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
        op.create_table(
        'Table',
        sa.Column('table_id', sa.Integer, primary_key=True),
        sa.Column('student_name', sa.String, nullable=False),
        sa.Column('math',sa.Integer),
        sa.Column('physics',sa.Integer),
        sa.Column('chemistry',sa.Integer)
     )


def downgrade():
    op.drop_table("Table")
    pass
