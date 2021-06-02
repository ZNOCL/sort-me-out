from datetime import date, datetime

from backend.app.app.crud.base import CRUDBase
from backend.app.app.models.booking import Booking
from backend.app.app.schemas.booking import BookingCreate, BookingUpdate

from typing import List

from sqlalchemy.orm import Session


class CRUDBooking(CRUDBase[Booking, BookingCreate, BookingUpdate]):
    def get_all_for_today(
            self, db: Session, *, skip: int = 0) -> List[Booking]:
        return (
            db.query(self.model)
                .filter(Booking.date == datetime.today().date())
                .offset(skip)
                .all()
        )


booking = CRUDBooking(Booking)
