from PIL import Image, ImageDraw, ImageFont


def draw_rectangle( position: tuple, lines: int ):
    draw = ImageDraw.Draw( img )
    draw.rectangle( (position[0] + 4, position[1], position[0] + 276, position[1] + lines * 30 - 5), fill=(66, 176, 245) )


def draw_name( position: tuple, text: str ):
    d = ImageDraw.Draw(img)
    w, h = d.textsize( text, font=names_font )
    position = (position[0] - w / 2, position[1] - h / 2)
    d.text( position, text, font=names_font, fill=(0, 0, 0))


def draw_hour( position: tuple, hours: int, minutes: int ):
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)

    text = str(hours) + ":" + minutes
    d = ImageDraw.Draw(img)
    d.text( position, text, font=hours_font, fill=(0, 0, 0))


DATA = (
    ("Alisa", 19, 00, "Monday", 60),
    ("Mateusz", 17, 00, "Tuesday", 60),
    ("Hania", 18, 40, "Tuesday", 60),
    ("Wojtek", 19, 40, "Tuesday", 60),
    ("Sebastian", 17, 00, "Wednesday", 90),
    ("Julka", 18, 30, "Wednesday", 60),
    ("Julka", 17, 00, "Friday", 60),
    ("Mania", 12, 00, "Saturday", 60),
    ("Sebastian", 13, 00, "Saturday", 60),
)

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

names_font = ImageFont.truetype("Arial.otf", 25)
hours_font = ImageFont.truetype("Arial.otf", 20)
img = Image.open("plain.png")

for record in DATA:
    x = 100 + DAYS.index( record[3] ) * 280
    y = 50 + (record[ 1 ] - 7) * 120 + record[ 2 ] // 15 * 30
    lines = record[4] // 15

    draw_rectangle( (x, y), lines )
    draw_name( (x + 140, y + lines // 2 * 30), record[0] )
    draw_hour( (x + 10, y + 5), record[1], record[2] )

img.save("result.png")
