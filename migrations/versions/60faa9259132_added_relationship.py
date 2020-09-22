"""added relationship

Revision ID: 60faa9259132
Revises: f37c2f9df90c
Create Date: 2020-09-22 09:53:31.268467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60faa9259132'
down_revision = 'f37c2f9df90c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###