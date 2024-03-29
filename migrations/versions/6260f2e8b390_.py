"""empty message

Revision ID: 6260f2e8b390
Revises: 56d3f9434a17
Create Date: 2024-03-28 13:43:34.877901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6260f2e8b390'
down_revision = '56d3f9434a17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###