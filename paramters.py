from enum import Enum


class StartTime(Enum):
    MONDAY = 0
    TODAY = 1
    TOMORROW = 2


DAYS = "PL"
# DAYS = "ENG"

HOUR_START = 10
HOUR_END = 20

# WRITE_DATES = False
WRITE_DATES = True

# START_WITH = StartTime.TODAY
START_WITH = StartTime.TOMORROW
# START_WITH = StartTime.MONDAY

THEME = "dark"
# THEME = "light"
