from PIL import Image, ImageDraw, ImageFont
import textwrap
from datetime import datetime, timedelta

THEME = "dark"
# THEME = "light"

COLORS = {
    "blue": (66, 176, 245),
    "black": (0, 0, 0),
    "gray": (47, 49, 67),
    "cyan": (0, 213, 255),
    "yellow": (252, 254, 220),
    "white": (252, 254, 252),
    "green": (84, 197, 132),
    "orange": (243, 154, 75),
    "red": (252, 99, 99),
    "pink": (174, 133, 238),
    "dark_theme_background": (27, 29, 41),
}

TYPES = {
    "l": "green",  # lecture
    "c": "pink",  # class
    "to": "blue",  # tutoring online
    "t": "blue",  # tutoring online
    "ts": "red",  # tutoring stationary
    "tv": "orange",  # tutoring variable (time)
    "r": "orange",  # tutoring variable (time)
}

TEXT_COLOR = COLORS["black"] if THEME == "light" else COLORS["white"]



COLUMN_WIDTH = 250
COLUMN_OFFSET = 125
ROW_HEIGHT = 40
ROW_OFFSET = 90

DAYS_EN = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
DAYS_PL = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")


names_font = ImageFont.truetype("Arial.otf", 25)
hours_font = ImageFont.truetype("Arial.otf", 23)
days_font = ImageFont.truetype("Arial.otf", 32)
labels_font = ImageFont.truetype("Arial.otf", 35)


today = datetime.today()
day_of_week = today.weekday()
next_days = [(today + timedelta(days=i)).strftime('%d.%m') for i in range(7)]
for i in range(7 - day_of_week):
    next_days = next_days[1:] + next_days[:1]