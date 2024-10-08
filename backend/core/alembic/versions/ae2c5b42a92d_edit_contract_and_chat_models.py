"""edit contract and chat models

Revision ID: ae2c5b42a92d
Revises: 76acca4254f5
Create Date: 2024-09-12 22:00:43.834536

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ae2c5b42a92d"
down_revision: Union[str, None] = "76acca4254f5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(
        op.f("fk_chats_contract_id_contracts"),
        "chats",
        "contracts",
        ["contract_id"],
        ["id"],
        ondelete="cascade",
    )
    op.drop_constraint("fk_contracts_chat_id_chats", "contracts", type_="foreignkey")
    op.drop_column("contracts", "chat_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "contracts",
        sa.Column("chat_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "fk_contracts_chat_id_chats", "contracts", "chats", ["chat_id"], ["id"]
    )
    op.drop_constraint(
        op.f("fk_chats_contract_id_contracts"), "chats", type_="foreignkey"
    )
    # ### end Alembic commands ###
