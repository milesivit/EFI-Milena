"""creacion marca

Revision ID: c2693c490b37
Revises: 
Create Date: 2024-07-29 19:19:00.548441

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c2693c490b37"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "marca",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("marca")
    # ### end Alembic commands ###
