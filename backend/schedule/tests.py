from datetime import datetime
from django.test import TestCase

from .utils import create_schedule


class TestScheduleNormal(TestCase):
    def test_schedule_normal(self):
        """
        Test that an appropriate sleep schedule is returned.
        """
        # Setup.
        work_tasks = [
            {
                "work_start": datetime(year=2020, month=10, day=3, hour=8),
                "work_end": datetime(year=2020, month=10, day=3, hour=17),
            },
            {
                "work_start": datetime(year=2020, month=10, day=4, hour=6),
                "work_end": datetime(year=2020, month=10, day=4, hour=15),
            },
            {
                "work_start": datetime(year=2020, month=10, day=5, hour=8),
                "work_end": datetime(year=2020, month=10, day=5, hour=17),
            },
            {
                "work_start": datetime(year=2020, month=10, day=6, hour=9),
                "work_end": datetime(year=2020, month=10, day=6, hour=18),
            },
            {
                "work_start": datetime(year=2020, month=10, day=7, hour=5),
                "work_end": datetime(year=2020, month=10, day=7, hour=14),
            },
        ]
        # Run.
        schedule = create_schedule(work_tasks)
        # Check.
        self.assertEqual(
            schedule,
            [
                {
                    "work_start": datetime(year=2020, month=10, day=3, hour=8),
                    "work_end": datetime(year=2020, month=10, day=3, hour=17),
                    "sleep_start": datetime(year=2020, month=10, day=3, hour=20),
                    "sleep_end": datetime(year=2020, month=10, day=4, hour=4),
                },
                {
                    "work_start": datetime(year=2020, month=10, day=4, hour=6),
                    "work_end": datetime(year=2020, month=10, day=4, hour=15),
                    "sleep_start": datetime(year=2020, month=10, day=4, hour=22),
                    "sleep_end": datetime(year=2020, month=10, day=5, hour=6),
                },
                {
                    "work_start": datetime(year=2020, month=10, day=5, hour=8),
                    "work_end": datetime(year=2020, month=10, day=5, hour=17),
                    "sleep_start": datetime(year=2020, month=10, day=5, hour=23),
                    "sleep_end": datetime(year=2020, month=10, day=6, hour=7),
                },
                {
                    "work_start": datetime(year=2020, month=10, day=6, hour=9),
                    "work_end": datetime(year=2020, month=10, day=6, hour=18),
                    "sleep_start": datetime(year=2020, month=10, day=6, hour=19),
                    "sleep_end": datetime(year=2020, month=10, day=7, hour=3),
                },
                {
                    "work_start": datetime(year=2020, month=10, day=7, hour=5),
                    "work_end": datetime(year=2020, month=10, day=7, hour=14),
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
