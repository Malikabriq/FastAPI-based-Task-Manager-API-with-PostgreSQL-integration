from sqlalchemy.orm import Session
from app.db import models
from app.schemas import tasks as schemas

def create_task(db: Session, task: schemas.Task):
    db_task = models.TaskDB(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(models.TaskDB).all()

def update_task(db: Session, task_id: str, updates: schemas.TaskUpdate):
    task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()
    if not task:
        return None
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: str):
    task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return True
