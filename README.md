# Growth-Assignment
 To create an assignment submission portal with the following functionality and structure.

## Requirements
- fastapi
- uvicorn
- pydantic
- pydantic-settings
- pymongo
- passlib
- bcrypt
- pyjwt

## Installation
This package uses Python 3.12.
```bash
python -m venv env
.\env\Scripts\Activate
pip install -r requirements.txt
```

## Code Structure
- The code structure being followed is the Model-Service-Controller architecture. Model comprises of the collection structure, Service comprises of the methods with business logic and validations, Controller comprises with methods with API endpoints.
- Error and input validations are done mostly in the Service layer methods, only upload-assignment method validation is done in the controller itself.
- Proper comments are provided to specify responsiblity of various methods/APIs.
- Further config.py consists of connection and authorization secrets and security.py consists of methods for proper authorization through bearer JWT token generation and decoding of those JWT token when endpoints are being hit to get access to user/admin details. These tokens are generated when login takes place after successful registration and time limit is of 120 minutes as of now.
- Database used is MongoDB.

## Run and Test the application
- Clone the github repository
- Pip install all the given requirements in virtual environment as provided in the installation part.
- To start the server, use command: `uvicorn main:app --reload`
- Hit the API's in this order: Post `http://127.0.0.1:8000/auth/register` \
  Sample input:
  ```bash
  {
    "username": "hoe_hoe",
    "email": "john@example.com",
    "password": "password123",
    "is_admin":true
  }
  ```
  Register for user as well (is_admin : false)
- Post `http://127.0.0.1:8000/auth/login` \
  Sample input:
  ```bash
  {
    "username": "hoe_hoe",
    "password": "password123"
  }
  ```
  This will generate the bearer JWT token for authorization. For admin APIs, use the admin login token and for user APIs, use the user login token.
- Post `http://127.0.0.1:8000/user/upload` \
  Sample input:
  ```bash
  {
    "userId":"john_doe",
    "task": "Complete the Python assignment",
    "admin": "hoe_hoe"
  }
  ```
  Initial status: Pending
- Get `http://127.0.0.1:8000/user/admins` \
  Sample input: No input
- Get `http://127.0.0.1:8000/admin/assignments` \
  Sample input: No input
- Put `http://127.0.0.1:8000/admin/assignments/reject?id` \
  Sample input:
  ```bash
  Query Params-
  id : 67083b9350ec2c02404fc044
  ```
- Put `http://127.0.0.1:8000/admin/assignments/accept?id` \
  Sample input:
  ```bash
  Query Params-
  id : 67083b9350ec2c02404fc044
  ```
- This the ideal order of API endpoint hitting to be followed.
  
  
