from fastapi import HTTPException
from pydantic import BaseModel, Field, ValidationError
from database import get_db
from bson import ObjectId
from datetime import datetime

db = get_db()

# get user by given username
def get_user_by_username(username: str):
    user = db.users.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# get admin by given admin name
def get_admin_by_username(username: str):
    admin = db.users.find_one({"username": username, "is_admin": True})
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin

# business logic for uploading an assignment
def upload_assignment(assignment_data, user):  

    # error and input checks for assignment upload are done in user_controller
    assignment = {
        "user_id": ObjectId(user['user_id']),
        "task": assignment_data['task'],
        "admin": ObjectId(assignment_data['admin']),
        "status": "pending",
        "timestamp": datetime.utcnow()
    }
    db.assignments.insert_one(assignment)

# logic to get list of all admins
def get_admins():
    admins = list(db.users.find({"is_admin": True}))
    if not admins:
        raise HTTPException(status_code=404, detail="No admins found")
    return [
        {
            "_id": str(admin["_id"]),
            "username": admin["username"],
            "email": admin["email"]
        }
        for admin in admins
    ]
