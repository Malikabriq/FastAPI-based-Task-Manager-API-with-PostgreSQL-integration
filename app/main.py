from fastapi import FastAPI
from app.db import database
from app.db.models import Base
from app.routers import tasks as task_router


# Initialize FastAPI
app = FastAPI(title="Task Manager API")

# Create database tables on startup
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=database.engine)

# Include Routers
app.include_router(task_router.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Task Manager API"}
