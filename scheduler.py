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
    "ts": "red",  # tutoring stationary
    "tv": "orange",  # tutoring variable (time)
}

TEXT_COLOR = COLORS["black"] if THEME == "light" else COLORS["white"]

COLUMN_WIDTH = 250
COLUMN_OFFSET = 125
ROW_HEIGHT = 40
ROW_OFFSET = 90


DAYS_EN = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
DAYS_PL = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
DAYS = DAYS_PL

today = datetime.today()
day_of_week = today.weekday()
next_days = [(today + timedelta(days=i)).strftime('%d.%m') for i in range(7)]
for i in range(7 - day_of_week):
    next_days = next_days[1:] + next_days[:1]

names_font = ImageFont.truetype("Arial.otf", 25)
hours_font = ImageFont.truetype("Arial.otf", 23)
days_font = ImageFont.truetype("Arial.otf", 32)
labels_font = ImageFont.truetype("Arial.otf", 35)

img = Image.new("RGB", (1875, 2200), (255, 255, 255))
draw = ImageDraw.Draw(img)


def draw_rectangle(position: tuple, type: str, lines: int):
    color = TYPES[type]
    x1, y1, x2, y2 = (
    position[0] + 4, position[1], position[0] + COLUMN_WIDTH - 4, position[1] + ROW_HEIGHT * lines - 4)
    draw.rounded_rectangle((x1, y1, x2, y2), fill=COLORS[color], width=2, outline=COLORS["black"], radius=20)
    return x2 - x1, y2 - y1


def draw_name(position: tuple, text: str, rec_size: tuple):
    # Calculate the available width for the text
    available_width = COLUMN_WIDTH + 150  # A margin of 20 pixels on each side

    # Wrap the text to fit the available width
    wrapped_text = textwrap.fill(text, width=int(available_width / 25))

    wrapped_text_width, wrapped_text_height = draw.multiline_textsize(wrapped_text, font=names_font)

    # Calculate the position to center the wrapped text on the image
    x = (rec_size[0] - wrapped_text_width) // 2
    y = (rec_size[1] - wrapped_text_height) // 2

    # Draw the centered wrapped text on the image
    draw.multiline_text((x + position[0], y + position[1]), wrapped_text, fill=TEXT_COLOR, font=names_font,
                        align='center')


def draw_hour(position: tuple, hours: int, minutes: int, duration: int):
    new_minutes = minutes + duration % 60

    new_hours = hours + duration // 60

    if new_minutes >= 60:
        new_hours += new_minutes // 60
        new_minutes %= 60

    if minutes < 10:
        minutes = "0" + str(minutes)

    if new_minutes < 10:
        new_minutes = "0" + str(new_minutes)

    text = f"{hours}:{minutes} - {new_hours}:{new_minutes}"
    d = ImageDraw.Draw(img)
    d.text(position, text, font=hours_font, fill=COLORS["white"])

DATA = (
    # ("Egzamin - C# (0056)", 14, 00, 2, 30, "c"),

    # ("Lena", 19, 00, 3, 60, "tv"),
    # ("Alisa", 18, 00, 2, 60, "to"),
    # ("Hania", 17, 00, 2, 60, "to"),
    # ("Pola", 18, 00, 2, 60, "to"),
    # ("Michał", 18, 30, 3, 60, "to"),
    # ("Sofia", 11, 00, 2, 60, "tv"),
    # ("Nikola", 14, 00, 3, 60, "to"),
    # ("Kaja", 16, 30, 1, 60, "tv"),
    ("Damian", 18, 00, 4, 60, "tv"),
    # ("Dawid", 17, 00, 5, 60, "tv"),
    ("Benjamin", 12, 00, 2, 60, "tv"),
    ("Maja", 17, 00, 2, 60, "tv"),
    # ("Nika", 18, 00, 2, 60, "tv"),
    # ("Dawid", 18, 00, 4, 120, "tv"),
    # ("Mania", 16, 00, "Friday", 60, "to"),

    # ("Mateusz", 16, 00, 3, 90, "ts"),

    # ("Marysia", 17, 00, 4, 60, "tv"),
    # ("Michał", 18, 00, 5, 90, "tv"),
    # ("Nika", 19, 30, "Monday", 60, "tv"),
    # ("Mateusz", 16, 00, 4, 90, "tv"),

)

img.paste(COLORS["dark_theme_background"], (0, 0, img.size[0], img.size[1]))
# gray rectangles
for i in range(3):
    height = ROW_OFFSET + ROW_HEIGHT * 4 + i * 16 * ROW_HEIGHT
    draw.rectangle((0, height, img.size[0], height + ROW_HEIGHT * 8), fill=COLORS["dark_theme_background"])

# day labels
for i, day in enumerate(DAYS):
    w, h = draw.textsize(day, font=days_font)
    position = (i * 250 + 250 - w / 2, 30 - h / 2)
    draw.text(position, day, font=days_font, fill=TEXT_COLOR)

for i, day in enumerate(next_days):
    w, h = draw.textsize(day, font=days_font)
    position = (i * 250 + 250 - w / 2, 60 - h / 2)
    draw.text(position, day, font=days_font, fill=TEXT_COLOR)


# horizontal lines
for i in range(0, 54, 4):
    height = i * ROW_HEIGHT + ROW_OFFSET
    draw.line((0, height, img.size[0], height), fill=TEXT_COLOR)

# vertical lines
for i in range(7):
    width = i * COLUMN_WIDTH + COLUMN_OFFSET
    draw.line((width, 0, width, img.size[1]), fill=TEXT_COLOR)

# hours
for i in range(8, 21):
    text = (str(i) if i > 9 else "0" + str(i)) + ":00"
    draw.text((30, (i - 8) * ROW_HEIGHT * 4 + ROW_OFFSET), text, font=labels_font, fill=TEXT_COLOR)

for record in DATA:
    x = COLUMN_OFFSET + (record[3] - 1) * COLUMN_WIDTH
    y = ROW_OFFSET + (record[1] - 8) * ROW_HEIGHT * 4 + record[2] // 15 * ROW_HEIGHT
    lines = record[4] // 15

    rec_size = draw_rectangle((x, y), record[5], lines)
    draw_name((x, y), record[0], rec_size)
    draw_hour((x + 10, y + 5), record[1], record[2], record[4])


def generate():
    img.save("result.png")


if __name__ == "__main__":
    generate()
