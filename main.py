from fastapi import FastAPI
from controller import auth_controller, user_controller, admin_controller
from database import connect_db

app = FastAPI()


connect_db()

# routes
app.include_router(auth_controller.router, prefix="/auth", tags=["Auth"])
app.include_router(user_controller.router, prefix="/user", tags=["User"])
app.include_router(admin_controller.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "Welcome to the Assignment Submission Portal!"}
