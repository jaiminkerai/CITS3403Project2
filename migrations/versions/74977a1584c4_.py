"""empty message

Revision ID: 74977a1584c4
Revises: 4b8267a20e53
Create Date: 2020-05-20 14:59:10.995497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74977a1584c4'
down_revision = '4b8267a20e53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('long_questions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.String(length=255), nullable=True),
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quizzes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('long_questions')
    # ### end Alembic commands ###