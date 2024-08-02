"""marca y modelo corregido

Revision ID: fa3a27a29c4a
Revises: 2cbc24763a19
Create Date: 2024-07-31 19:11:47.198546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa3a27a29c4a'
down_revision = '2cbc24763a19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modelo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('marca_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'marca', ['marca_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modelo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('marca_id')

    # ### end Alembic commands ###
