from sqlalchemy import Column, Time, UniqueConstraint, Date, Integer

from backend.app.app.db.session import Base


class Holiday(Base):
    __tablename__ = "holidays"
    __table_args__ = (UniqueConstraint('date', 'start'),)

    date = Column(Date, primary_key=True)
    start = Column(Time, primary_key=True)
    end = Column(Time)

class DaySlots(Base):
    __tablename__ = "day_slots"
    __table_args__ = (UniqueConstraint('weekday', 'start'),)

    weekday = Column(Integer, primary_key=True)
    start = Column(Time, primary_key=True)
    end = Column(Time)
