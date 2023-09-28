from PIL import Image, ImageDraw, ImageFont
import textwrap

COLORS = {
    "blue": (66, 176, 245),
    "black": (0, 0, 0),
    "gray": (228, 230, 228),
    "cyan": (84, 245, 232),
    "yellow": (252, 254, 220),
    "white": (252, 254, 252),
    "green": (66, 245, 155),
    "orange": (245, 183, 49),
}

TYPES = {
    "l": "yellow",  # lecture
    "c": "white",  # class
    "to": "blue",  # tutoring online
    "ts": "green",  # tutoring stationary
    "tv": "orange",  # tutoring variable (time)
}

COLUMN_WIDTH = 250
COLUMN_OFFSET = 125
ROW_HEIGHT = 40
ROW_OFFSET = 90


def draw_rectangle(position: tuple, type: str, lines: int):
    color = TYPES[type]
    x1, y1, x2, y2 = (
    position[0] + 4, position[1], position[0] + COLUMN_WIDTH - 4, position[1] + ROW_HEIGHT * lines - 4)
    draw.rectangle((x1, y1, x2, y2), fill=COLORS[color], width=2, outline=COLORS["black"])
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
    draw.multiline_text((x + position[0], y + position[1]), wrapped_text, fill=(0, 0, 0), font=names_font,
                        align='center')


def draw_hour(position: tuple, hours: int, minutes: int):
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)

    text = str(hours) + ":" + minutes
    d = ImageDraw.Draw(img)
    d.text(position, text, font=hours_font, fill=(0, 0, 0))


DATA = (
    ("Angielski (0074)", 10, 00, "Monday", 90, "c"),
    ("Programowanie funkcyjne (0053)", 8, 15, "Monday", 90, "c"),
    ("Programowanie w C# i .NET (0056)", 12, 00, "Monday", 90, "c"),
    ("Angielski (0074)", 10, 00, "Wednesday", 90, "c"),
    ("Android (0020)", 10, 00, "Thursday", 90, "c"),
    ("Projekt zespołowy (0016)", 13, 00, "Thursday", 45, "c"),
    ("Wzorce projektowe (0056)", 8, 00, "Friday", 90, "c"),

    ("Android (0009)", 8, 15, "Tuesday", 90, "l"),
    ("Programowanie funkcyjne (1177)", 8, 15, "Wednesday", 90, "l"),
    ("Programowanie w C# i .NET (1093)", 12, 15, "Wednesday", 90, "l"),
    ("Wzorce projektowe (1177)", 8, 15, "Thursday", 90, "l"),

    ("Alisa", 18, 30, "Monday", 60, "to"),
    ("Hania", 17, 00, "Tuesday", 60, "to"),
    ("Mania", 16, 00, "Friday", 60, "to"),

    ("Mateusz", 12, 00, "Saturday", 90, "ts"),
    ("Paweł", 13, 30, "Saturday", 90, "ts"),

    ("Sofia", 19, 00, "Tuesday", 60, "tv"),
    ("Martyna", 12, 00, "Friday", 60, "tv"),
    # ("Marysia", 12, 00, "Friday", 60, "tv"),

)

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

names_font = ImageFont.truetype("Arial.otf", 25)
hours_font = ImageFont.truetype("Arial.otf", 23)
days_font = ImageFont.truetype("Arial.otf", 42)
labels_font = ImageFont.truetype("Arial.otf", 35)

# img = Image.open("plain.jpg")
#

# img.save("result.png")

img = Image.new("RGB", (1875, 2200), (255, 255, 255))
draw = ImageDraw.Draw(img)

# gray rectangles
for i in range(3):
    height = ROW_OFFSET + ROW_HEIGHT * 4 + i * 16 * ROW_HEIGHT
    draw.rectangle((0, height, img.size[0], height + ROW_HEIGHT * 8), fill=COLORS["gray"])

# day labels
for i, day in enumerate(DAYS):
    w, h = draw.textsize(day, font=days_font)
    position = (i * 250 + 250 - w / 2, 50 - h / 2)
    draw.text(position, day, font=days_font, fill=(0, 0, 0))

# horizontal lines
for i in range(54):
    height = i * ROW_HEIGHT + ROW_OFFSET
    draw.line((0, height, img.size[0], height), fill=COLORS["black"])

# vertical lines
for i in range(7):
    width = i * COLUMN_WIDTH + COLUMN_OFFSET
    draw.line((width, 0, width, img.size[1]), fill=COLORS["black"])

# hours
for i in range(8, 21):
    text = (str(i) if i > 9 else "0" + str(i)) + ":00"
    draw.text((30, (i - 8) * ROW_HEIGHT * 4 + ROW_OFFSET), text, font=labels_font, fill=(0, 0, 0))

for record in DATA:
    x = COLUMN_OFFSET + DAYS.index(record[3]) * COLUMN_WIDTH
    y = ROW_OFFSET + (record[1] - 8) * ROW_HEIGHT * 4 + record[2] // 15 * ROW_HEIGHT
    lines = record[4] // 15

    rec_size = draw_rectangle((x, y), record[5], lines)
    draw_name((x, y), record[0], rec_size)
    draw_hour((x + 10, y + 5), record[1], record[2])

img.save("result.png")
