from datetime import time, date

from pydantic import BaseModel


class HolidayBase(BaseModel):
    _date: date
    start: time
    end: time


# Properties to receive on Holiday creation from user
class HolidayCreate(HolidayBase):
    pass


# Properties to receive on Holiday update from user
class HolidayUpdate(HolidayBase):
    pass


# Properties shared by Holiday models stored in DB
class HolidayInDBBase(BaseModel):
    _date: date
    start: time
    end: time

    # Pydantic accepts ORM object in addition to dict as input
    class Config:
        orm_mode = True


# Properties to return to client
class Holiday(HolidayInDBBase):
    pass


# Properties stored in DB
class HolidayInDB(HolidayInDBBase):
    pass
