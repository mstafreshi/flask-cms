"""empty message

Revision ID: ebda7167d0aa
Revises: 0e1c7f712cec
Create Date: 2023-04-20 14:56:51.405982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebda7167d0aa'
down_revision = '0e1c7f712cec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('meta_keywords', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('meta_description', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('meta_description')
        batch_op.drop_column('meta_keywords')

    # ### end Alembic commands ###
