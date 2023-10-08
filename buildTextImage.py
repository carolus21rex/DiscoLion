from PIL import Image, ImageDraw, ImageFont

def text_to_png(text, w, h, font_size=24):
    # Specify the image size (width and height) in pixels
    width, height = w, h

    # Create a new image with a transparent background (RGBA)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # The last value (alpha) is set to 0 for transparency

    # Create a drawing object to add text to the image
    draw = ImageDraw.Draw(img)

    # Font color (RGB)
    text_color = (0, 0, 0)  # NOT White

    # Calculate the text size and position within the image using font.getbbox()
    bbox = draw.textbbox((0, 0), text, font=None)
    x = (width - bbox[2] - bbox[0]) / 2
    y = (height - bbox[3] - bbox[1]) / 2

    # Create a font object with the specified font size and boldness
    font_path = "C:\\Windows\\Fonts\\comic.ttf"  # Path to Comic Sans MS font on Windows
    custom_font = ImageFont.truetype(font_path, font_size)

    # Add the text to the image
    draw.text((x, y), text, fill=text_color, font=custom_font)

    return img


