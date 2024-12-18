"""adminn

Revision ID: 22d660e84a31
Revises: f0f4ff57a30f
Create Date: 2024-09-24 21:52:50.138390

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "22d660e84a31"
down_revision = "f0f4ff57a30f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("is_admin", sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_column("is_admin")

    # ### end Alembic commands ###
