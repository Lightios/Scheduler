from PIL import Image, ImageDraw, ImageFont

COLORS = {
    "blue": (66, 176, 245),
    "black": (0, 0, 0),
    "gray": (228, 230, 228),
    "cyan": (84, 245, 232),
    "yellow": (252, 254, 220),
    "white": (252, 254, 252)
}

COLUMN_WIDTH = 250
COLUMN_OFFSET = 125
ROW_HEIGHT = 40
ROW_OFFSET = 90


def draw_rectangle( position: tuple, type: str, lines: int ):
    color = {"t": "blue", "l": "yellow", "c": "white"}[type]
    draw.rectangle( (position[0] + 4, position[1], position[0] + COLUMN_WIDTH - 4, position[1] + ROW_HEIGHT * lines - 4),
                    fill=COLORS[ color ], width=2, outline=COLORS["black"] )


def draw_name( position: tuple, text: str ):
    w, h = draw.textsize( text, font=names_font )
    position = (position[0] - w / 2, position[1] - h / 2)
    draw.text( position, text, font=names_font, fill=(0, 0, 0))


def draw_hour( position: tuple, hours: int, minutes: int ):
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)

    text = str(hours) + ":" + minutes
    d = ImageDraw.Draw(img)
    d.text( position, text, font=hours_font, fill=(0, 0, 0))


DATA = (
    ("Sebastian", 15, 00, "Monday", 90, "t"),
    ("Julek", 17, 00, "Monday", 60, "t"),
    ("Alisa", 18, 30, "Tuesday", 60, "t"),
    ("Wojtek", 19, 30, "Tuesday", 60, "t"),
    ("Julek", 17, 00, "Wednesday", 60, "t"),
    ("Julek", 15, 00, "Thursday", 60, "t"),
    ("Hania", 18, 15, "Thursday", 60, "t"),
    ("Mania", 12, 00, "Saturday", 60, "t"),
    # ("Sebastian", 13, 00, "Saturday", 60, "t"),

    ("SK (1073)", 17, 45, "Monday", 90, "c"),
    ("MN (0016)", 16, 00, "Tuesday", 90, "c"),
    ("Angielski (1103)", 10, 15, "Wednesday", 90, "c"),
    ("JFA (0073)", 12, 15, "Wednesday", 90, "c"),
    ("IO (0056)", 10, 30, "Thursday", 135, "c"),
    ("RPS (0083)", 8, 30, "Friday", 90, "c"),
    ("Angielski (0074)", 10, 15, "Friday", 90, "c"),

    ("SK (0089)", 12, 00, "Monday", 90, "l"),
    ("MN (0004)", 8, 30, "Tuesday", 90, "l"),
    ("RPS (0089)", 14, 15, "Thursday", 90, "l"),
    ("IO (0089)", 13, 00, "Friday", 90, "l"),
    ("JFA (0089)", 14, 45, "Friday", 90, "l")
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
for i in range( 3 ):
    height = ROW_OFFSET + ROW_HEIGHT * 4 + i * 16 * ROW_HEIGHT
    draw.rectangle( (0, height, img.size[0], height + ROW_HEIGHT * 8), fill=COLORS["gray"] )

# day labels
for i, day in enumerate( DAYS ):
    w, h = draw.textsize( day, font=days_font )
    position = (i * 250 + 250 - w / 2, 50 - h / 2)
    draw.text( position, day, font=days_font, fill=(0, 0, 0))

# horizontal lines
for i in range( 54 ):
    height = i * ROW_HEIGHT + ROW_OFFSET
    draw.line( (0, height, img.size[0], height), fill=COLORS["black"] )

# vertical lines
for i in range( 7 ):
    width = i * COLUMN_WIDTH + COLUMN_OFFSET
    draw.line( (width, 0, width, img.size[1]), fill=COLORS["black"] )

# hours
for i in range( 8, 21 ):
    text = (str(i) if i > 9 else "0" + str(i)) + ":00"
    draw.text( (30, (i - 8) * ROW_HEIGHT * 4 + ROW_OFFSET), text, font=labels_font, fill=(0, 0, 0))

for record in DATA:
    x = COLUMN_OFFSET + DAYS.index( record[3] ) * COLUMN_WIDTH
    y = ROW_OFFSET + ( record[ 1 ] - 8 ) * ROW_HEIGHT * 4 + record[ 2 ] // 15 * ROW_HEIGHT
    lines = record[ 4 ] // 15

    draw_rectangle( (x, y), record[ 5 ], lines )
    draw_name( (x + COLUMN_WIDTH // 2, int(y + ROW_HEIGHT * lines / 2)), record[ 0 ] )
    draw_hour( (x + 10, y + 5), record[ 1 ], record[ 2 ] )


img.save("result.png")
