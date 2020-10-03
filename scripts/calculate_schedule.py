from datetime import datetime, time, timedelta
import pprint

work_tasks = [
    (
        datetime(year=2020, month=10, day=3, hour=12),
        datetime(year=2020, month=10, day=3, hour=21),
    ),
    (
        datetime(year=2020, month=10, day=4, hour=6),
        datetime(year=2020, month=10, day=4, hour=15),
    ),
    (
        datetime(year=2020, month=10, day=5, hour=8),
        datetime(year=2020, month=10, day=5, hour=17),
    ),
    (
        datetime(year=2020, month=10, day=6, hour=10),
        datetime(year=2020, month=10, day=6, hour=19),
    ),
    (
        datetime(year=2020, month=10, day=7, hour=5),
        datetime(year=2020, month=10, day=7, hour=19),
    ),
]


def calculate_schedule(work_tasks):
    """
    Rough function for producing a schedule based on a series of work tasks.
    Input:
        work_tasks - [(work1_start, work1_end), (work2_start, work2_end)...]
    Output:
        [[(work1_start, work1_end), (sleep1_start, sleep1_end), (nap1_start, nap2_end)]...]
        [[(work1_start, work1_end), (sleep1_start, sleep1_end), None]...]

    """
    output = []
    sleep_debt = timedelta()
    for i in range(len(work_tasks)):
        nap = None
        # Extract today's work task
        day = work_tasks[i]
        work_task_start = day[0]
        work_task_end = day[1]

        # If not the final day
        if i < len(work_tasks) - 1:
            # Find next day's start of work
            next_work_task_start = work_tasks[i + 1][0]
            # Wake up 2hrs before work
            sleep_end = next_work_task_start - timedelta(hours=2)
            # Find ideal starting point for sleep
            sleep_start = sleep_end - timedelta(hours=8)

            # If work conflicts with ideal sleep, sleep later and add to sleep debt
            if work_task_end > sleep_start:
                sleep_start = work_task_end + timedelta(hours=1)
                sleep_debt = sleep_debt + timedelta(hours=8) - (sleep_end - sleep_start)

        if sleep_debt.total_seconds() > 0:
            # Calculate after work gap, allowing for wind down time
            after_work_gap = (work_task_end - sleep_start) - timedelta(1)
            # Nap starts 1hr after work
            nap_start = work_task_end + timedelta(hours=1)

            # If the sleep debt is bigger than the available gap
            if sleep_debt >= after_work_gap:
                nap_end = nap_start + after_work_gap
                sleep_debt = sleep_debt - after_work_gap
            else:
                nap_end = nap_start + sleep_debt
                # Reset sleep debt to 0
                sleep_debt = timedelta()
            nap = (nap_start, nap_end)
        output.append([day, (sleep_start, sleep_end), nap])
    return output


prty = pprint.PrettyPrinter()
prty.pprint(calculate_schedule(work_tasks))
