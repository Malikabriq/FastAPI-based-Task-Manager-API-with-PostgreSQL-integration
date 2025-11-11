from sqlalchemy import Column, String, Float, Enum, Integer
from app.db.database import Base
import enum

class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class StatusEnum(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(Enum(PriorityEnum), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)
    estimated_hours = Column(Float, nullable=False)
    hours_spent = Column(Float, nullable=False)
    progress = Column(Integer, nullable=False, default=0.0)
    verdict = Column(String, nullable=True)
