from PIL import Image, ImageDraw
import textwrap

from paramters import *
from data import DATA


def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def draw_rectangle(position: tuple, type: str, lines: int):
    color = TYPES[type]
    x1, y1, x2, y2 = (position[0] + 4, position[1] + 4, position[0] + COLUMN_WIDTH - 4, position[1] + ROW_HEIGHT * lines - 4)
    draw.rounded_rectangle((x1, y1, x2, y2), fill=COLORS[color], width=2, outline=COLORS["black"], radius=20)
    return x2 - x1, y2 - y1

def draw_name(position: tuple, text: str, rec_size: tuple):
    available_width = COLUMN_WIDTH + 150

    wrapped_text = textwrap.fill(text, width=int(available_width / 25))

    wrapped_text_width, wrapped_text_height = textsize(wrapped_text, font=names_font)

    x = (rec_size[0] - wrapped_text_width) // 2
    y = (rec_size[1] - wrapped_text_height) // 2

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


def draw_background():
    # gray rectangles
    for i in range(3):
        height = ROW_OFFSET + ROW_HEIGHT * 4 + i * 16 * ROW_HEIGHT
        draw.rectangle((0, height, img.size[0], height + ROW_HEIGHT * 8), fill=COLORS["dark_theme_background"])

    # day labels
    for i, day in enumerate(DAYS):
        w, h = textsize(day, font=days_font)
        position = (i * 250 + 250 - w / 2, 30 - h / 2)
        draw.text(position, day, font=days_font, fill=TEXT_COLOR)

    for i, day in enumerate(next_days):
        w, h = textsize(day, font=days_font)
        position = (i * 250 + 250 - w / 2, 60 - h / 2)
        # draw.text(position, day, font=days_font, fill=TEXT_COLOR)

    # horizontal lines
    for i in range(0, HOUR_END - HOUR_START + 1):
        height = i * ROW_HEIGHT * 4 + ROW_OFFSET
        draw.line((0, height, img.size[0], height), fill=TEXT_COLOR, width=2)

    # vertical lines
    for i in range(7):
        width = i * COLUMN_WIDTH + COLUMN_OFFSET
        draw.line((width, 0, width, img.size[1]), fill=TEXT_COLOR, width=2)

    # hours
    for i in range(HOUR_START, HOUR_END + 1):
        text = (str(i) if i > 9 else "0" + str(i)) + ":00"
        draw.text((30, (i - HOUR_START) * ROW_HEIGHT * 4 + ROW_OFFSET), text, font=labels_font, fill=TEXT_COLOR)


def draw_data():
    for record in DATA:
        x = COLUMN_OFFSET + (record[3] - 1) * COLUMN_WIDTH
        y = ROW_OFFSET + (record[1] - HOUR_START) * ROW_HEIGHT * 4 + record[2] // 15 * ROW_HEIGHT
        lines = record[4] // 15

        rec_size = draw_rectangle((x, y), record[5], lines)
        draw_name((x, y), record[0], rec_size)
        draw_hour((x + 10, y + 5), record[1], record[2], record[4])


img = Image.new("RGB", (1875, ROW_OFFSET + ROW_HEIGHT * 4 * (HOUR_END - HOUR_START + 1)), (255, 255, 255))
draw = ImageDraw.Draw(img)


def generate():
    img.paste(COLORS["dark_theme_background"], (0, 0, img.size[0], img.size[1]))

    draw_background()
    draw_data()
    img.save("result.png")


if __name__ == "__main__":
    generate()
