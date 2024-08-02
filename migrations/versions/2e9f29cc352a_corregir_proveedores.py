"""corregir proveedores

Revision ID: 2e9f29cc352a
Revises: 0579d151ca66
Create Date: 2024-07-30 12:13:04.259658

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2e9f29cc352a'
down_revision = '0579d151ca66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.alter_column('telefono',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=50),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.alter_column('telefono',
               existing_type=sa.String(length=50),
               type_=mysql.INTEGER(display_width=11),
               nullable=True)

    # ### end Alembic commands ###
