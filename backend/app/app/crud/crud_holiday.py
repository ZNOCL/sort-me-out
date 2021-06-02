class CRUDBooking(CRUDBase[Holiday, BookingCreate, BookingUpdate]):
    def get_all_for_today(
            self, db: Session, *, skip: int = 0) -> List[Booking]:
        return (
            db.query(self.model)
                .filter(Booking.date == datetime.today().date())
                .offset(skip)
                .all()
        )


booking = CRUDBooking(Booking)
