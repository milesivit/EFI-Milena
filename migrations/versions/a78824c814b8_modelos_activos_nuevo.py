"""modelos activos nuevo

Revision ID: a78824c814b8
Revises: 1376886f87d4
Create Date: 2024-07-31 15:45:16.485175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a78824c814b8'
down_revision = '1376886f87d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modelo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activo', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modelo', schema=None) as batch_op:
        batch_op.drop_column('activo')

    # ### end Alembic commands ###
