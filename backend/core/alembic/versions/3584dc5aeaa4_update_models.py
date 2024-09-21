"""update models

Revision ID: 3584dc5aeaa4
Revises: a4cf4333bf4f
Create Date: 2024-09-21 21:57:24.494467

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3584dc5aeaa4"
down_revision: Union[str, None] = "a4cf4333bf4f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "chat_to_user",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("chat_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["chat_id"], ["chats.id"], name=op.f("fk_chat_to_user_chat_id_chats")
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_chat_to_user_user_id_users")
        ),
        sa.PrimaryKeyConstraint("user_id", "chat_id", name=op.f("pk_chat_to_user")),
    )
    op.drop_table("association_table")
    op.drop_constraint("fk_messages_receiver_id_users", "messages", type_="foreignkey")
    op.drop_column("messages", "receiver_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "messages",
        sa.Column("receiver_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "fk_messages_receiver_id_users", "messages", "users", ["receiver_id"], ["id"]
    )
    op.create_table(
        "association_table",
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("chat_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["chat_id"], ["chats.id"], name="fk_association_table_chat_id_chats"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_association_table_user_id_users"
        ),
        sa.PrimaryKeyConstraint("user_id", "chat_id", name="pk_association_table"),
    )
    op.drop_table("chat_to_user")
    # ### end Alembic commands ###
