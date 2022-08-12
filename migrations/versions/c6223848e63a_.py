"""empty message

Revision ID: c6223848e63a
Revises: cee92b065bc4
Create Date: 2022-08-12 20:57:43.006736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6223848e63a'
down_revision = 'cee92b065bc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=250), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.String(length=10), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###
