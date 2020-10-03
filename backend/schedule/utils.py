from datetime import datetime, timedelta


def create_schedule(schedule):
    """Generate a schedule based on daily work tasks.

    Args:
        tasks (list of dictionaries): Daily work tasks.

    Returns:
        (list of dictionaries): Full daily schedule.
    """
    sleeps = len(schedule) - 1
    for i in range(sleeps):
        # Get lower and upper bounds for sleep.
        earliest = schedule[i]["work_end"]
        latest = schedule[i + 1]["work_start"]
        # Get next sleep block.
        sleep_block = create_sleep_block(earliest, latest, sleep_required=8)
        schedule[i]["sleep_start"] = sleep_block["sleep_start"]
        schedule[i]["sleep_end"] = sleep_block["sleep_end"]
    return schedule


def create_sleep_block(earliest, latest, sleep_required=8):
    """Allocates a sleep block based on time constraints.

    Args:
        lower_bound (datetime): Lower bound for allocating a sleep block.
        upper_bound (datetime): Upper bound for a sleep block.
        sleep_required (int, optional): Hours of sleep required. Defaults to 8.

    Returns:
        dictionary: Suitable start and end time sfor sleep, and a possible sleep debt.
    """
    # Set base arguments.
    sleep_debt = 0
    lower_bound = earliest + timedelta(hours=1)
    upper_bound = latest - timedelta(hours=2)
    # Wake up 2 hours before first work task.
    sleep_end = upper_bound
    # Start sleeping 8 hours before waking up.
    sleep_start = sleep_end - timedelta(hours=sleep_required)
    # If sleep overlaps work, push forwards and collect debt.
    if sleep_start < lower_bound:
        sleep_start = lower_bound
        sleep_debt = sleep_required - (sleep_end - sleep_start).total_seconds() // 3600
    result = {
        "sleep_start": sleep_start,
        "sleep_end": sleep_end,
        "sleep_debt": sleep_debt,
    }
    return result


def create_nap_block(earliest, latest):
    pass


def create_eating_blocks(earliest, latest):
    pass


def create_exercise_blocks(earliest, latest):
    pass
