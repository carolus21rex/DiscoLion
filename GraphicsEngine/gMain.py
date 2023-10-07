import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600

# Create the display window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Scaled Image Display")

current_directory = os.getcwd()

# Load the image
image_path = os.path.join(current_directory, 'images', 'savana.png')
image = pygame.image.load(image_path)

# Get the new dimensions based on the scaling factor
new_width = int(screen_width)
new_height = int(screen_height)

# Scale the image
scaled_image = pygame.transform.scale(image, (new_width, new_height))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the scaled image
    screen.blit(scaled_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()




