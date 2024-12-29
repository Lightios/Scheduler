from paramters import *

from PIL import ImageFont
from datetime import datetime, timedelta

COLORS = {
    "blue": (66, 176, 245),
    "black": (0, 0, 0),
    "gray": (47, 49, 67),
    "cyan": (0, 213, 255),
    "yellow": (255, 235, 13),
    "white": (252, 254, 252),
    "green": (84, 197, 132),
    "orange": (243, 154, 75),
    "red": (252, 99, 99),
    "pink": (230, 112, 128),
    "claret": (120, 8, 60),
    "dark_theme_background": (27, 29, 41),
}

TYPES = {
    # "l": "green",  # lecture
    # "c": "pink",  # class
    # "to": "blue",  # tutoring online
    # "t": "blue",  # tutoring online
    # "ts": "red",  # tutoring stationary
    # "tv": "green",  # tutoring variable (time)
    # "r": "orange",  # tutoring variable (time)
    # "black": "black",
    "p": "pink",  # primary school
    "hb": "green",  # high school - base
    "he": "orange",  # high school - extended
    "m": "blue",  # matura

    # "p": "green",  # primary school
    # "m": "orange",  # matura
    # "hb": "red",  # high school - base
    # "he": "claret",  # high school - extended
}

TEXT_COLOR = COLORS["black"] if THEME == "light" else COLORS["white"]
LINES_COLOR = COLORS["black"] if THEME == "light" else COLORS["gray"]

COLUMN_WIDTH = 250
COLUMN_OFFSET = 125
ROW_HEIGHT = 40
ROW_OFFSET = 90

DAYS_EN = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
DAYS_PL = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")

DAYS = DAYS_EN if DAYS == "ENG" else DAYS_PL

names_font = ImageFont.truetype("Arial.otf", 25)
hours_font = ImageFont.truetype("Arial.otf", 23)
days_font = ImageFont.truetype("Arial.otf", 32)
labels_font = ImageFont.truetype("Arial.otf", 35)

match START_WITH:
    case StartTime.TODAY:
        today = datetime.today()
    case StartTime.TOMORROW:
        today = (datetime.today() + timedelta(days=1)).strftime('%d.%m')
    case _:
        today = datetime.strptime(START_WITH, '%d.%m.%Y')
# today = datetime.today()
#
# if START_WITH == StartTime.TOMORROW:
#     today += timedelta(days=1)

day_of_week = today.weekday()
next_days = [(today + timedelta(days=i)).strftime('%d.%m') for i in range(7)]
for i in range(7 - day_of_week):
    next_days = next_days[1:] + next_days[:1]


DAYS = DAYS[day_of_week:] + DAYS[:day_of_week]
next_days = next_days[day_of_week:] + next_days[:day_of_week]

STARTING_DAY = day_of_week + 1 # if START_WITH in (StartTime.TODAY, StartTime.TOMORROW) else 1
