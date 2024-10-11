from fastapi import APIRouter, Depends, HTTPException
from typing import Dict
from controller.auth_controller import get_current_user
from service.user_service import upload_assignment, get_admins
from service.user_service import get_admin_by_username


router = APIRouter()

# API for user to upload assignment
@router.post("/upload")
def upload(assignment: Dict[str, str], current_user: dict = Depends(get_current_user)):
    if current_user['username'] != assignment.get('userId'):
        raise HTTPException(status_code=403, detail="You can only upload assignments for your own user ID")
    
    admin = get_admin_by_username(assignment.get('admin'))
    if not admin:
        raise HTTPException(status_code=400, detail="Invalid admin username")
    
    assignment_data = {
        "task": assignment.get('task'),
        "admin": str(admin['_id'])
    }

    upload_assignment(assignment_data, current_user)
    return {"msg": "Assignment uploaded successfully"}

# API to get list of all admins
@router.get("/admins")
def list_admins():
    return get_admins()
