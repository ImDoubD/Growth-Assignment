from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

# assignment model in database with initial state of assignment as pending 
class AssignmentModel(BaseModel):
    id: ObjectId
    user_id: ObjectId
    task: str
    admin: ObjectId
    status: str = "pending"  #accept or reject
    timestamp: datetime
