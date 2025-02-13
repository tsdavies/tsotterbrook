"""Add timestamp column to BlogPost

Revision ID: 6727b62f496a
Revises: 
Create Date: 2024-12-29 18:04:57.187349

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6727b62f496a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("blog_post", schema=None) as batch_op:
        batch_op.add_column(sa.Column("timestamp", sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("blog_post", schema=None) as batch_op:
        batch_op.drop_column("timestamp")

    # ### end Alembic commands ###
