from datetime import time, date, datetime
from typing import Optional

from pydantic import BaseModel, Field

from backend.app.app.models import TaskStatus


class BookingBase(BaseModel):
    event: str = Field(..., max_length=200, min_length=1)
    effort: Optional[int] = Field(1, title='task effort', le=12)
    slot: Optional[datetime] = None


# Properties to receive on Booking creation from user
class BookingCreate(BookingBase):
    pass


# Properties to receive on Booking update from user
class BookingUpdate(BookingBase):
    pass


# Properties shared by Booking models stored in DB
class BookingInDBBase(BaseModel):
    _date: date
    start: time
    end: time
    event: str
    status: TaskStatus

    # Pydantic accepts ORM object in addition to dict as input
    class Config:
        orm_mode = True

# Properties to return to client
class Booking(BookingInDBBase):
    pass


# Properties stored in DB
class BookingInDB(BookingInDBBase):
    pass
