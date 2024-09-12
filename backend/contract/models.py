from typing import Optional

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.sqlalchemy import Base

from datetime import datetime

from messenger.models import Chat
from users.models import User


class Contract(Base):
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    contractor_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    chat: Mapped[Optional[Chat]] = relationship(uselist=False)
    customer: Mapped[User] = relationship(uselist=False, foreign_keys="Contract.customer_id")
    contractor: Mapped[User] = relationship(uselist=False, foreign_keys="Contract.contractor_id")
