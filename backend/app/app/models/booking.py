from enum import Enum

from sqlalchemy import Column, Integer, String, Time, Date

from backend.app.app.db.session import Base


class TaskStatus(str, Enum):
    DONE = 'done'
    IN_PROGRESS = 'in progress'
    MISSED = 'missed'
    PENDING = 'pending'


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, unique=True)


class Booking(Base):
    __tablename__ = "bookings"
    date = Column(Date, primary_key=True)
    start = Column(Time, primary_key=True)
    end = Column(Time)
    event = Column(String)
    status = Column(String, index=True, default=TaskStatus.PENDING)
