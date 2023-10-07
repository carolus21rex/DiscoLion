from PIL import Image

def buildImage(background, overlay_path, x, y, xsize, ysize):
    # Open the background image and overlay image
    overlay = Image.open(overlay_path)

    # Ensure both images have the same size (optional)
    overlay = overlay.resize((xsize, ysize))

    # Create a copy of the background image
    result = background.copy()

    # Paste the overlay image onto the result image at the specified coordinates (x, y)
    result.paste(overlay, (x, y), overlay)

    # Convert the result image to RGBA format if needed
    result = result.convert('RGBA')

    # Return the resulting image
    return result
