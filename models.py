from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    """User model."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Task(Base):
    """Task model."""
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Integer, default=0)

# schemas.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    """User creation schema."""
    username: str
    password: str

class User(BaseModel):
    """User schema."""
    id: int
    username: str

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    """Task creation schema."""
    title: str
    description: str

class TaskUpdate(BaseModel):
    """Task update schema."""
    title: str = None
    description: str = None
    completed: int = None

class Task(BaseModel):
    """Task schema."""
    id: int
    title: str
    description: str
    completed: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    """User login schema."""
    username: str
    password: str
```