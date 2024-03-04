from enum import Enum


class StartTime(Enum):
    MONDAY = 0
    TODAY = 1
    TOMORROW = 2


DAYS = "PL"
# DAYS = "ENG"

HOUR_START = 10
HOUR_END = 20

WRITE_DATES = True
START_WITH = StartTime.TOMORROW

THEME = "dark"
# THEME = "light"
