from collections import defaultdict
from datetime import datetime
from schemas import Task, TaskStatus

tasks_db = defaultdict(lambda: defaultdict(dict))


def current_datetime_str():
    now = datetime.now()
    day_mon_date = now.strftime("%a, %b, %d")
    today = now.strftime('%Y%m%d')
    hr = now.strftime("%-H")
    mnt = now.strftime("%-M")
    apm = now.strftime("%p")
    return {
        "today": today,
        'day_mon_date': day_mon_date,
        "hr": hr,
        "mnt": mnt,
        "apm": apm
    }


def update_today_slots():
    cds = current_datetime_str()
    today_tasks = tasks_db.get(cds['today'], {})
    for slot, task_dict in today_tasks.get('booked', {}).items():

        # Mark elapsed tasks
        if slot[4:6] < cds['hr']:
            task_dict['status'] = TaskStatus.MISSED
        # Mark inprogress tasks
        elif slot[:2] < cds['hr']:
            task_dict['status'] = TaskStatus.IN_PROGRESS

    free_slots = [slot for slot in today_tasks.get('free', []) if slot[4:6] >= cds['hr']]

    if free_slots == []:
        # first_time
        print(f"Creating slots since I got {today_tasks.get('free')}")
        free_slots = [f'{hr}00{hr + 1}00' for hr in range(int(cds['hr']) + 1, 24)]

    tasks_db[cds['today']]['free'] = free_slots

    return cds


def get_today_bookings():
    timestamp = update_today_slots()
    return tasks_db[timestamp['today']]


def book_appointment(task: Task):
    timestamp = update_today_slots()
    today_calendar = tasks_db[timestamp['today']]
    booked_slots = today_calendar['booked']
    free_slots = today_calendar['free']
    # booked_tasks = [info.get('name') for slot, info in booked_slots.items()]
    for h in range(task.effort):
        tasks_db[timestamp['today']]['booked'][free_slots[h]] = {"name": task.name,
                                                                 "status": task.status}
        tasks_db[timestamp['today']]['free'].remove(free_slots[h])

    return booked_slots
