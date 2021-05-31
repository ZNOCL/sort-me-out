from fastapi import FastAPI, Body, HTTPException
from schemas import Task
from crud import book_appointment, get_today_bookings

app = FastAPI()


@app.get("/")
def root():
    return {"Smarty": "Wanna sort out the mess?!"}


@app.get("/tasks/{name}")
def root(name):
    task = Task(name=name)
    return book_appointment(task)


@app.post("/tasks")
def create_task(task: Task = Body(..., embed=True)):
    return book_appointment(task)


@app.put("/tasks")
def update_task(task: Task = Body(..., embed=True)):
    # try:
    #     db[task.name]['target'] = task.slot or "updated_target"
    # except KeyError:
    #     raise HTTPException(status_code=404, detail="no task found by that name")
    # return db.get(task.name)
    return {}


@app.get("/tasks")
def retrieve_task():
    # return {k: v.get("target") for k, v in db.items()}
    return get_today_bookings()


@app.delete("/tasks")
def delete_task(task: Task = Body(..., embed=True)):
    # try:
    #     del db[task.name]
    # except KeyError:
    #     return {"error": "no task found by that name!"}
    return {}
