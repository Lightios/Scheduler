from enum import Enum


class StartTime(Enum):
    TODAY = 1
    TOMORROW = 2


DAYS = "PL"
# DAYS = "ENG"

HOUR_START = 11
HOUR_END = 19

# WRITE_DATES = False
WRITE_DATES = True

# START_WITH = StartTime.TODAY
# START_WITH = StartTime.TOMORROW
START_WITH = "02.01.2025"

THEME = "dark"
# THEME = "light"
