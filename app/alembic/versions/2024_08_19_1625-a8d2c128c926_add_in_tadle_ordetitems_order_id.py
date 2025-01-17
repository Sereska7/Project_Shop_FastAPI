"""Add in tadle OrdetItems order_id

Revision ID: a8d2c128c926
Revises: 11524997ba04
Create Date: 2024-08-19 16:25:48.421983

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a8d2c128c926"
down_revision: Union[str, None] = "11524997ba04"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("orderitems", sa.Column("order_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "orderitems", "orders", ["order_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "orderitems", type_="foreignkey")
    op.drop_column("orderitems", "order_id")
    # ### end Alembic commands ###
