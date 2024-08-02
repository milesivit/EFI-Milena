"""fabricantes y modelos

Revision ID: ea671edb85df
Revises: 2e9f29cc352a
Create Date: 2024-07-30 19:38:17.675471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea671edb85df'
down_revision = '2e9f29cc352a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fabricante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('pais_origen', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modelo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('fabricante_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fabricante_id'], ['fabricante.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('modelo')
    op.drop_table('fabricante')
    # ### end Alembic commands ###
