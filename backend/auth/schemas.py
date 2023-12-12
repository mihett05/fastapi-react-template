from beanie import Document


class User(Document):
    username: str
    email: str
    hashed_password: str
