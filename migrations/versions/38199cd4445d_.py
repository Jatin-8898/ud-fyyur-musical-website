"""empty message

Revision ID: 38199cd4445d
Revises: b91fb084cc2b
Create Date: 2020-05-13 20:32:18.274650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38199cd4445d'
down_revision = 'b91fb084cc2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###
