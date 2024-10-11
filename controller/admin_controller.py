from fastapi import APIRouter, Depends, Query
from service.admin_service import get_assignments, accept_assignment, reject_assignment
from controller.auth_controller import get_current_user

router = APIRouter()

# API to get all the assignments
@router.get("/assignments")
def view_assignments(admin=Depends(get_current_user)):
    return get_assignments(admin['user_id'])


# API to accept the assignment as per the id provided
@router.put("/assignments/accept")
def accept(id: str = Query(...), admin=Depends(get_current_user)):
    accept_assignment(id)
    return {"msg": "Assignment accepted"}

# API to accept the assignment as per the id provided
@router.put("/assignments/reject")
def reject(id: str = Query(...), admin=Depends(get_current_user)):
    reject_assignment(id)
    return {"msg": "Assignment rejected"}
