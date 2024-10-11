from pydantic import BaseModel, EmailStr
from bson import ObjectId

# user model in database with initial status of being admin false
class UserModel(BaseModel):
    id: ObjectId
    username: str
    email: EmailStr
    password: str
    is_admin: bool = False
