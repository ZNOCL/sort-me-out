from datetime import datetime
from typing import List

from fastapi import FastAPI, Body, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.app.app.crud import crud
from backend.app.app.crud.crud import NoSlotException, get_booked_slots
from backend.app.app.db.session import SessionLocal, engine
from backend.app.app.schemas import booking

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.exception_handler(NoSlotException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": "You are too busy, no free slot for next 7 days"}),
    )


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root(db: Session = Depends(get_db)):
    # crud.create_day_slots(db)
    return {"Smarty": "Wanna sort out the mess?!"}


@app.get("/tasks", response_model=List[schemas.booking.Booking])
def get_tasks(db: Session = Depends(get_db)):
    bookings = get_booked_slots(db, datetime.now())
    return bookings


@app.post("/tasks", response_model=booking.Booking)
def create_task(task: schemas.Task = Body(...), db: Session = Depends(get_db)):
    return crud.create_task(db, datetime.now(), task)

# @app.put("/tasks")
# def update_task(task: Task = Body(..., embed=True)):
#     # try:
#     #     db[task.name]['target'] = task.slot or "updated_target"
#     # except KeyError:
#     #     raise HTTPException(status_code=404, detail="no task found by that name")
#     # return db.get(task.name)
#     return {}
#
#
# @app.get("/tasks")
# def retrieve_task():
#     # return {k: v.get("target") for k, v in db.items()}
#     return get_today_bookings()
#
#
# @app.delete("/tasks")
# def delete_task(task: Task = Body(..., embed=True)):
#     # try:
#     #     del db[task.name]
#     # except KeyError:
#     #     return {"error": "no task found by that name!"}
#     return {}
