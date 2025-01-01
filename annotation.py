from PIL import Image, ImageDraw, ImageFont

from constants import TYPES, COLORS


def create_annotated_image(output_path):
    # Define the size of the image
    width, height = 300, 110
    image = Image.new('RGB', (width, height), COLORS['dark_theme_background'])
    draw = ImageDraw.Draw(image)

    # Define colors and corresponding texts
    annotations = [
        (COLORS[TYPES["p"]], 'Szkoła podstawowa'),
        (COLORS[TYPES["m"]], 'Matura'),
        (COLORS[TYPES["hb"]], 'Szkoła średnia - podstawa'),
        (COLORS[TYPES["he"]], 'Szkoła średnia - rozszerzenie'),
    ]

    # Define the size of the square and the font
    square_size = 15
    margin = 10
    font = ImageFont.truetype("Arial.otf", 15)

    # Draw the squares and text
    for i, (color, text) in enumerate(annotations):
        y = i * (square_size + margin) + margin
        draw.rectangle([10, y, 10 + square_size, y + square_size], fill=color)
        draw.text((30, y), text, fill=color, font=font)

    # Save the image
    image.save(output_path)


# Create the annotated image
create_annotated_image('annotated_image.png')