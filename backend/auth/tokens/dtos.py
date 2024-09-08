from dataclasses import dataclass
from datetime import datetime


@dataclass
class TokenPairDto:
    access_token: str
    refresh_token: str


@dataclass
class TokenInfo:
    subject: str
    expires_in: datetime
