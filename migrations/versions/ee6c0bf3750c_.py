"""empty message

Revision ID: ee6c0bf3750c
Revises: aa7f37526ffc
Create Date: 2018-12-19 03:42:21.922310

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ee6c0bf3750c'
down_revision = 'aa7f37526ffc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('file', 'data',
               existing_type=postgresql.BYTEA(),
               type_=sa.String(),
               existing_nullable=True)
    op.alter_column('user', 'photo',
               existing_type=sa.VARCHAR(),
               type_=sa.String(length=100),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'photo',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.alter_column('file', 'data',
               existing_type=sa.String(),
               type_=postgresql.BYTEA(),
               existing_nullable=True)
    # ### end Alembic commands ###
