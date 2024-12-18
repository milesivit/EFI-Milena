"""activo marca

Revision ID: f65221b1e9e1
Revises: ea671edb85df
Create Date: 2024-07-31 14:57:19.168474

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f65221b1e9e1"
down_revision = "ea671edb85df"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("marca", schema=None) as batch_op:
        batch_op.add_column(sa.Column("activo", sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("marca", schema=None) as batch_op:
        batch_op.drop_column("activo")

    # ### end Alembic commands ###
