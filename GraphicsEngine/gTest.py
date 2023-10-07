import pygame
import sys
import os
import time
from PIL import Image
import gMain as BI

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600

# Create the display window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Overlay Example")

current_directory = os.getcwd()

# Load the background image
background_path = os.path.join(current_directory, 'images', 'savana.png')
background = Image.open(background_path)

# Load the overlay image
lion_path = os.path.join(current_directory, 'images', 'lion.png')
overlay = pygame.image.load(lion_path)

# Get the new dimensions based on the scaling factor
new_width = screen_width
new_height = screen_height



x, y = 0, 0
lastTime = time.time_ns()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    if (time.time_ns() > lastTime + 100000000):
        x += 1
        y += 1
        lastTime = time.time_ns()
        if x == 300:
            x = 0
            y = 0

    # Call the buildImage function to create a composite image
    composite_image = BI.buildImage(background, lion_path, x, y, 200, 150)
    # Convert the composite image to a Pygame surface
    composite_surface = pygame.image.fromstring(composite_image.tobytes(), composite_image.size, composite_image.mode)

    scaled_background = pygame.transform.scale(composite_surface, (new_width, new_height))
    # Convert the composite image to a Pygame surface

    # Draw the scaled background image
    # screen.blit(scaled_background, (0, 0))

    # Draw the composite surface at the specified (x, y) coordinates
    screen.blit(scaled_background, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
