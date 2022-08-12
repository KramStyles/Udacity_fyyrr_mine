"""empty message

Revision ID: b50a9315f6c0
Revises: 6137205f9285
Create Date: 2022-08-12 21:10:09.145970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b50a9315f6c0'
down_revision = '6137205f9285'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'show_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Venue', 'show_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'show_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Artist', 'show_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
