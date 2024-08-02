"""moproveedor activo

Revision ID: bf5b7e26917c
Revises: a50a7ec49313
Create Date: 2024-07-31 17:45:27.895392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf5b7e26917c'
down_revision = 'a50a7ec49313'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activo', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.drop_column('activo')

    # ### end Alembic commands ###
