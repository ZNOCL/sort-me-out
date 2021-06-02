from datetime import datetime, time, timedelta

import models
from schemas import Task
from sqlalchemy.orm import Session


class NoSlotException(Exception):
    pass


def create_day_slots(db: Session):
    for weekday in range(7):
        for slot in range(18, 23):
            day_slot = models.DaySlots(weekday=weekday,
                                       start=time(slot),
                                       end=time(slot + 1))
            db.add(day_slot)
    db.commit()


def get_booked_slots(db: Session, date: datetime):
    return db.query(models.Booking).filter(models.Booking.date == date.date()).all()


def get_free_slots(db: Session, date: datetime):
    day_slots = db.query(models.DaySlots).filter(models.DaySlots.weekday == date.weekday()).all()
    booked_slots = [slot.start for slot in get_booked_slots(db, date)]

    # Free Slots = Day Slots not booked and comes after current hour and
    free_slots = [slot for slot in day_slots if slot.start not in booked_slots and slot.start > date.time()]
    return free_slots


def create_task(db: Session, date: datetime, task: Task):
    # Try for next 7 days
    for i in range(7):
        date += timedelta(days=i)
        free_slots = get_free_slots(db, date)
        if free_slots:
            break
    else:
        raise NoSlotException("No Free slot available for next 7 days")
    # TODO - handle task effort
    # TODO - handle preferred time range of task
    db_booking = models.Booking(date=date,
                                start=free_slots[0].start,
                                end=free_slots[0].end,
                                event=task.name)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

#
# def current_datetime_str():
#     now = datetime.now()
#     day_mon_date = now.strftime("%a, %b, %d")
#     today = now.strftime('%Y%m%d')
#     hr = now.strftime("%-H")
#     mnt = now.strftime("%-M")
#     apm = now.strftime("%p")
#     return {
#         "today": today,
#         'day_mon_date': day_mon_date,
#         "hr": hr,
#         "mnt": mnt,
#         "apm": apm
#     }
#
