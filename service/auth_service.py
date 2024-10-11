from fastapi import HTTPException
from pydantic import EmailStr, ValidationError
from security import hash_password, verify_password, create_access_token
from database import get_db

db = get_db()


def validate_registration_data(data):
    if "username" not in data or not data["username"]:
        raise HTTPException(status_code=400, detail="Username is required.")
    if "email" not in data or not data["email"]:
        raise HTTPException(status_code=400, detail="Email is required.")
    if "password" not in data or not data["password"]:
        raise HTTPException(status_code=400, detail="Password is required.")
    
    try:
        # Pydantic's EmailStr type to validate email format
        EmailStr.validate(data["email"])
    except ValidationError:
        raise HTTPException(status_code=400, detail="Invalid email format.")

    # Ensure password meets minimum length
    if len(data["password"]) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters long.")

# logic to register a user with password being kept hashed
def register_user(data):
    # Validate the input data
    validate_registration_data(data)
    
    # Check if the username or email is already taken
    if db.users.find_one({"username": data["username"]}) or db.users.find_one({"email": data["email"]}):
        raise HTTPException(status_code=400, detail="Username or email is already taken.")
    
    hashed_password = hash_password(data['password'])
    user = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password,
        "is_admin": data.get('is_admin', False)
    }
    db.users.insert_one(user)


# Logic to authenticate a user during login
def authenticate_user(username, password):
    # Check if the username exists
    user = db.users.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    # Verify the password
    if not verify_password(password, user['password']):
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    
    token = create_access_token({"user_id": str(user['_id']), "username": username})
    return {"access_token": token}