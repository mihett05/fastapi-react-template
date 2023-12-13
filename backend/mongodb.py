from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import get_config

from auth.schemas import User


async def init_mongodb():
    config = get_config()
    client = AsyncIOMotorClient(
        f"mongodb://{config.mongodb_user}:{config.mongodb_password}@localhost:27017"
    )

    await init_beanie(database=client.db, document_models=[User])
