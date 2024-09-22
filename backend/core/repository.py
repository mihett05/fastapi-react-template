from datetime import datetime
from types import NoneType
from typing import Iterable

from core.pydantic import PydanticModel
from core.sqlalchemy import Base


class BaseRepository:
    default_updated_types = {int, str, bool, datetime, NoneType}

    @staticmethod
    async def update_model_attrs(model: Base, dto: PydanticModel) -> Base:
        attrs = dto.model_dump().keys()
        for attr in attrs:
            new = getattr(dto, attr, None)
            old = getattr(model, attr, None)

            if type(new) not in BaseRepository.default_updated_types:
                continue

            setattr(model, attr, new or old)

        return model
