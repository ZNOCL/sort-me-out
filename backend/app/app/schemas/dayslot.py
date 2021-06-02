from datetime import time, date

from pydantic import BaseModel


class DaySlotBase(BaseModel):
    weekday: str
    start: time
    end: time


# Properties to receive on DaySlot creation from user
class DaySlotCreate(DaySlotBase):
    pass


# Properties to receive on DaySlot update from user
class DaySlotUpdate(DaySlotBase):
    pass


# Properties shared by DaySlot models stored in DB
class DaySlotInDBBase(BaseModel):
    start: time
    end: time

    # Pydantic accepts ORM object in addition to dict as input
    class Config:
        orm_mode = True


# Properties to return to client
class DaySlot(DaySlotInDBBase):
    weekday: str


# Properties stored in DB
class DaySlotInDB(DaySlotInDBBase):
    weekday: int
