from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import uuid4

from pydantic import Field, BaseModel


class TaskStatus(str, Enum):
    DONE = 'done'
    IN_PROGRESS = 'in progress'
    MISSED = 'missed'
    PENDING = 'pending'


class Task(BaseModel):
    name: str = Field(..., max_length=200, min_length=1)
    effort: Optional[int] = Field(1, title='task effort', le=12)
    slot: Optional[datetime] = None
    status: TaskStatus = TaskStatus.PENDING