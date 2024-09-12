from datetime import datetime, timezone

from adaptix.conversion import ConversionRetort, coercer


def convert_datetime(dt: datetime) -> datetime:
    if dt.tzinfo is None:  # Если datetime - time naive (из алхимии)
        return dt.replace(tzinfo=timezone.utc)
    return dt.replace(tzinfo=None)  # datetime - time aware (из pydantic)


sqlalchemy_retort = ConversionRetort(recipe=[coercer(datetime, datetime, convert_datetime)])
