"""empty message

Revision ID: 20c3bdf30f91
Revises: ebda7167d0aa
Create Date: 2023-04-23 22:49:23.304214

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '20c3bdf30f91'
down_revision = 'ebda7167d0aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=mysql.TEXT(),
               type_=mysql.LONGTEXT(),
               existing_nullable=False)
        batch_op.alter_column('body_html',
               existing_type=mysql.TEXT(),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('body_html',
               existing_type=mysql.LONGTEXT(),
               type_=mysql.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('body',
               existing_type=mysql.LONGTEXT(),
               type_=mysql.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
