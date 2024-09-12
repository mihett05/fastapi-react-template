"""add profile model

Revision ID: 429fbe7b6da4
Revises: b4707e7de4d0
Create Date: 2024-09-12 15:50:13.162281

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "429fbe7b6da4"
down_revision: Union[str, None] = "b4707e7de4d0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profiles",
        sa.Column("org_name", sa.String(), nullable=False),
        sa.Column("contact_phone", sa.String(), nullable=False),
        sa.Column("ceo_fullname", sa.String(), nullable=False),
        sa.Column("inn", sa.String(), nullable=False),
        sa.Column("kpp", sa.String(), nullable=False),
        sa.Column("ogrn", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_profiles_user_id_users"), ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_profiles")),
        sa.UniqueConstraint("contact_phone", name=op.f("uq_profiles_contact_phone")),
        sa.UniqueConstraint("org_name", name=op.f("uq_profiles_org_name")),
        sa.UniqueConstraint("user_id", name=op.f("uq_profiles_user_id")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("profiles")
    # ### end Alembic commands ###
