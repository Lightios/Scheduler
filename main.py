from PIL import Image, ImageDraw, ImageFont


def draw_rectangle( position: tuple ):
    draw = ImageDraw.Draw( img )
    draw.rectangle( (position[0] + 4, position[1], position[0] + 276, position[1] + 115), fill=(66, 176, 245) )


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
    ("Alisa", 19, 00, "Monday"),
    ("Mateusz", 17, 00, "Tuesday"),
    ("Hania", 19, 00, "Tuesday"),
    ("Sebastian", 17, 00, "Wednesday"),
    ("Wojtek", 18, 30, "Wednesday"),
    ("Julka", 17, 00, "Friday"),
    ("Mania", 12, 00, "Saturday"),
    ("Sebastian", 13, 00, "Saturday"),
)

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

names_font = ImageFont.truetype("Arial.otf", 25)
hours_font = ImageFont.truetype("Arial.otf", 20)
img = Image.open("plain.png")

for record in DATA:
    x = 100 + DAYS.index( record[3] ) * 280
    y = 50 + (record[ 1 ] - 7) * 120 + record[ 2 ] // 15 * 30

    draw_rectangle( (x, y) )
    draw_name( (x + 140, y + 60), record[0] )
    draw_hour( (x + 10, y + 5), record[1], record[2] )


img.save("result.png")
