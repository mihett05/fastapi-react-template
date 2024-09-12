"""add profile model

Revision ID: c0de27de7581
Revises: 5383aa742dc6
Create Date: 2024-09-12 15:12:39.628607

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c0de27de7581"
down_revision: Union[str, None] = "5383aa742dc6"
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
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("fk_profiles_user_id_users"), ondelete="cascade"),
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
