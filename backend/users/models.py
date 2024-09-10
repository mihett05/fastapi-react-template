from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.sqlalchemy import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    salt: Mapped[str]

    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    # profile: Mapped["Profile"] = relationship()


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    org_name: Mapped[str] = mapped_column(unique=True)
    contact_phone: Mapped[str] = mapped_column(unique=True)
    ceo_fullname: Mapped[str]
    inn: Mapped[str]
    kpp: Mapped[str]
    ogrn: Mapped[str]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="cascade"),
        primary_key=True, unique=True
    )
