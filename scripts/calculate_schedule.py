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

        # Calculate ideal sleep
        sleep_start = work_task_end + timedelta(hours=2)
        sleep_end = sleep_start + timedelta(hours=8)

        # If there is sleep debt from previous day
        if i > 0:
            if sleep_debt.total_seconds() / 3600 > 0:
                # Find the gap between waking up and work
                prev_sleep_end = work_tasks[i - 1][1]
                pre_work_gap = work_task_start - prev_sleep_end
                # If there is room for a nap, and time to wake up, fit in the morning
                if pre_work_gap < sleep_debt + timedelta(hours=1):
                    nap = (
                        prev_sleep_end,
                        prev_sleep_end
                        + timedelta(hours=sleep_debt + timedelta(hours=1)),
                    )
                    # Set sleep debt back to null
                    sleep_debt = timedelta()
                else:
                    # Otherwise add it to the end of sleep.
                    # If this is not possible, it will be caught in the next block.
                    sleep_end = sleep_end + timedelta(
                        hours=sleep_debt.total_seconds() / 3600
                    )
                    sleep_debt = timedelta()

        # If not the last day, look for conflicts with tomorrow's work task
        if i < len(work_tasks) - 1:
            next_work_task_start = work_tasks[i + 1][0]
            # Do they clash?

            if next_work_task_start < sleep_end:
                # Adjust sleep end to not conflict. Note sleep debt to be added to next day as nap.
                sleep_end = next_work_task_start - timedelta(hours=2)
                sleep_debt = sleep_end - sleep_start

        output.append([day, (sleep_start, sleep_end), nap])
    return output


prty = pprint.PrettyPrinter()
prty.pprint(calculate_schedule(work_tasks))
