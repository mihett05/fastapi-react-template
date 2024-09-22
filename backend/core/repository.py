from typing import Iterable

from core.pydantic import PydanticModel
from core.sqlalchemy import Base


class BaseRepository:

    @staticmethod
    async def update_model_attrs(model: Base, dto: PydanticModel) -> Base:
        attrs = dto.model_dump().keys()
        for attr in attrs:
            new = getattr(dto, attr)
            old = getattr(model, attr)

            if isinstance(new, Iterable) or isinstance(old, Iterable):
                continue
            setattr(model, attr, new or old)

        return model
