"""update models

Revision ID: a4cf4333bf4f
Revises: f2fde52e47c9
Create Date: 2024-09-21 18:42:45.424234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4cf4333bf4f'
down_revision: Union[str, None] = 'f2fde52e47c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association_table',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chats.id'], name=op.f('fk_association_table_chat_id_chats')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_association_table_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'chat_id', name=op.f('pk_association_table'))
    )
    op.add_column('chats', sa.Column('name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chats', 'name')
    op.drop_table('association_table')
    # ### end Alembic commands ###
