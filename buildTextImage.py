from PIL import Image, ImageDraw, ImageFont

def text_to_png(text):
    # Specify the image size (width and height) in pixels
    width, height = 400, 200

    # Create a new image with a transparent background (RGBA)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # The last value (alpha) is set to 0 for transparency

    # Create a drawing object to add text to the image
    draw = ImageDraw.Draw(img)

    # You can specify a TTF font file (e.g., 'arial.ttf') or use a built-in font
    font = ImageFont.load_default()

    # Font size in points
    font_size = 24

    # Text color (RGB)
    text_color = (0, 0, 0)  # Black

    # Calculate the text size and position within the image using font.getbbox()
    bbox = draw.textbbox((0, 0), text, font=font)
    x = (width - bbox[2] - bbox[0]) / 2
    y = (height - bbox[3] - bbox[1]) / 2

    # Add the text to the image
    draw.text((x, y), text, fill=text_color, font=font)

    return img
