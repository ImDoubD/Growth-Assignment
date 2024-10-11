from fastapi import HTTPException
from database import get_db
from bson import ObjectId

db = get_db()

def validate_object_id(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail=f"Invalid ID format: {id}")
    return ObjectId(id)


# service/business logic for getting the tagged assignment list
def get_assignments(admin_id: str):
    # Validate the admin_id
    admin_object_id = validate_object_id(admin_id)

    assignments = db.assignments.find({"admin": admin_object_id})
    assignment_list = []
    for assignment in assignments:
        assignment['_id'] = str(assignment['_id'])
        assignment['admin'] = str(assignment['admin'])
        assignment['user_id'] = str(assignment['user_id'])
        assignment_list.append(assignment)

    if not assignment_list:
        raise HTTPException(status_code=404, detail="No assignments found for this admin.")

    return assignment_list

# Logic to accept assignment according to the given id
def accept_assignment(assignment_id: str):
    assignment_object_id = validate_object_id(assignment_id)

    # Update the assignment status to "accepted"
    result = db.assignments.update_one(
        {"_id": assignment_object_id},
        {"$set": {"status": "accepted"}}
    )

    # Check if the update was successful
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Assignment not found.")
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Assignment was already accepted.")


# logic to reject assignment according to given id
def reject_assignment(assignment_id: str):
    assignment_object_id = validate_object_id(assignment_id)

    # Update the assignment status to "rejected"
    result = db.assignments.update_one(
        {"_id": assignment_object_id},
        {"$set": {"status": "rejected"}}
    )

    # Check if the update was successful
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Assignment not found.")
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Assignment was already rejected.")
