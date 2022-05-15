"""change user model fields

Revision ID: ae69d36f8b8b
Revises: f3d84c73b589
Create Date: 2022-05-15 15:37:53.794302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae69d36f8b8b'
down_revision = 'f3d84c73b589'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(), nullable=True))
    op.drop_column('users', 'comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('comments', sa.VARCHAR(), nullable=True))
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###