import pygame
import pymunk
import sys

# Initialize Pygame
pygame.init()

# Game Variables
nameOfGame = "Disco Lion Game"
heightOfDropLimit = 200
commonLength = 50
groundHeight =10
groundThickness = 10
tickCount = 0
score = 0
groundCutoff = 300

# Set up the Pygame window
screen_width, screen_height = 1024, 529
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(nameOfGame)

# Background image
bg = pygame.image.load("background.png")

# Create a Pymunk space
space = pymunk.Space()
space.gravity = (0, -100)  # Set gravity

# Create a ground segment
ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)

ground_segment = pymunk.Segment(ground_body, (groundCutoff, groundHeight), (screen_width-groundCutoff, groundHeight), groundThickness)
ground_segment.friction = 1
ground_body.friction = 1
space.add(ground_body, ground_segment)  # Add the ground body and segment to the space

# Lists to hold shapes
circles = []
rectangles = []
triangles = []
squares = []
shapes_to_remove = []

# Function to spawn a circle
def spawn_circle(pos): 
    if pos[1] > heightOfDropLimit:
        print("Didn't spawn shape because it was too close to the ground")
    else:
        circle_mass = 1
        circle_radius = 20
        circle_moment = pymunk.moment_for_circle(circle_mass, 0, circle_radius)
        circle_body = pymunk.Body(circle_mass, circle_moment)
        circle_body.position = pos
        circle_shape = pymunk.Circle(circle_body, circle_radius)
        circle_shape.friction = 0.7
        space.add(circle_body, circle_shape)
        circles.append(circle_shape)
        print(f"Circle spawned at position: {circle_body.position}")

# Function to spawn a triangle
def spawn_triangle(pos):
    if pos[1] > heightOfDropLimit:
        print("Didn't spawn shape because it was too close to the ground")
    else:
        triangle_base = commonLength
        triangle_height = commonLength # Adjust the side length of the triangle as needed

        # Define the vertices of an right triangle
        vertices = [
            (0, 0),
            (triangle_base, 0),
            (0, triangle_height)
            
        ]

        # Adjust the position to center the triangle at the given position
        triangle_position = (pos[0], screen_height - pos[1] - triangle_base / 2)

        # Create a body and add it to the space
        triangle_mass = 1
        triangle_moment = pymunk.moment_for_poly(triangle_mass, vertices, (0, 0))
        triangle_body = pymunk.Body(triangle_mass, triangle_moment)
        triangle_body.position = triangle_position

        # Create a triangle shape
        triangle_shape = pymunk.Poly(triangle_body, vertices)

        # Set friction for the triangle
        triangle_shape.friction = 0.7  # Adjust friction as needed

        # Add the triangle body and shape to the space
        space.add(triangle_body, triangle_shape)

        # Append the triangle shape to a list if needed
        triangles.append(triangle_shape)

        print(f"Triangle spawned at position: {triangle_body.position}")

# Function to spawn a rectangle
def spawn_rectangle(pos):
    if pos[1] > heightOfDropLimit:
        print("Didn't spawn shape because it was too close to the ground")
    else:
        rect_width = commonLength*2
        rect_height = commonLength

        # Adjust the position to center the rectangle at the mouse position
        rect_position = (pos[0] - rect_width // 2, screen_height - pos[1] - rect_height // 2)

        rect_mass = 1
        rect_moment = pymunk.moment_for_box(rect_mass, (rect_width, rect_height))
        rect_body = pymunk.Body(rect_mass, rect_moment)
        rect_body.position = rect_position
        rect_shape = pymunk.Poly.create_box(rect_body, (rect_width, rect_height))
        space.add(rect_body, rect_shape)
        rect_body.friction = 1
        rect_shape.friction = 0.7
        rectangles.append(rect_shape)
        print(f"Rectangle spawned at position: {rect_body.position}")

def spawn_square(pos):
    if pos[1] > heightOfDropLimit:
        print("Didn't spawn shape because it was too close to the ground")
    else:
        square_length = commonLength
        

        # Adjust the position to center the rectangle at the mouse position
        rect_position = (pos[0] - square_length // 2, screen_height - pos[1] - square_length // 2)

        rect_mass = 1
        rect_moment = pymunk.moment_for_box(rect_mass, (square_length, square_length))
        rect_body = pymunk.Body(rect_mass, rect_moment)
        rect_body.position = rect_position
        rect_shape = pymunk.Poly.create_box(rect_body, (square_length, square_length))
        space.add(rect_body, rect_shape)
        rect_body.friction = 0.7
        rect_shape.friction = 0.7
        squares.append(rect_shape)
        print(f"Square spawned at position: {rect_body.position}")

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_c:  # Press 'C' to spawn a circle
            #    spawn_circle(pygame.mouse.get_pos())
            if event.key == pygame.K_r:  # Press 'R' to spawn a rectangle
                spawn_rectangle(pygame.mouse.get_pos())
            elif event.key == pygame.K_t:  # Press 'T' to spawn a triangle
                spawn_triangle(pygame.mouse.get_pos())
            elif event.key == pygame.K_p:
                print(f"{pygame.mouse.get_pos()}")
            elif event.key == pygame.K_s:
                spawn_square(pygame.mouse.get_pos())

    # Update Pymunk space
    space.step(1 / 60)
    tickCount = tickCount + 1
    seconds = (int)(tickCount/60)
    # Clear the screen
    screen.fill([255, 255, 255])
    screen.blit(bg, (0, 0))
    myFont = pygame.font.SysFont("Times New Roman", 18)
    timerStr = "Stopwatch: " + str(seconds)
    timerLabel = myFont.render(timerStr, seconds, (0,0,0))
    screen.blit(timerLabel, (900, 20))
    # Draw the ground
    pygame.draw.line(screen, (0, 0, 0), (groundCutoff, screen_height - groundHeight), (screen_width-groundCutoff, screen_height- groundHeight), groundThickness)
    # Draw drop limit
    pygame.draw.line(screen, (255, 0, 0), (0, heightOfDropLimit), (screen_width, heightOfDropLimit), 3)

    # Draw the shapes
    for circle in circles:
        pygame.draw.circle(screen, (0, 0, 255), (int(circle.body.position.x), int(screen_height - circle.body.position.y)), int(circle.radius))
    for rect in rectangles:
        # Convert vertices to screen coordinates
        points = [(int(rect.body.position.x + point.x), int(screen_height - (rect.body.position.y + point.y))) for point in rect.get_vertices()]
        #Schedule rectangle for removal
        if rect.body.position.y < -100:  # Adjust the threshold as needed
            shapes_to_remove.append(rect)
        # Draw the rectangle
        pygame.draw.polygon(screen, (0, 0, 255), points)

    for triangle in triangles:
        # Get the vertices in world coordinates
        vertices = [triangle.body.local_to_world(v) for v in triangle.get_vertices()]
        #Schedule triangle for removal
        if triangle.body.position.y < -100:  # Adjust the threshold as needed
            shapes_to_remove.append(triangle)
        # Convert world coordinates to screen coordinates
        points = [(int(point.x), int(screen_height - point.y)) for point in vertices]

        # Draw the triangle
        pygame.draw.polygon(screen, (255, 0, 0), points)
    for sqr in squares:
        # Convert vertices to screen coordinates
        points = [(int(sqr.body.position.x + point.x), int(screen_height - (sqr.body.position.y + point.y))) for point in sqr.get_vertices()]
        #Schedule Square to be deleted
        if sqr.body.position.y < -100:  # Adjust the threshold as needed
            shapes_to_remove.append(sqr)
        # Draw the rectangle
        pygame.draw.polygon(screen, (0, 255, 0), points)
    for shape in shapes_to_remove:
        score=score-1
        if shape in squares:
            squares.remove(shape)
        elif shape in rectangles:
            rectangles.remove(shape)
        elif shape in triangles:
            triangles.remove(shape)
        shapes_to_remove.remove(shape)
        
    print(squares)
    score = len(squares) + len(rectangles) + len(triangles)
    scoreStr = "Score: " + str(score)
    scoreLabel = myFont.render(scoreStr, score, (0,0,0))
    screen.blit(scoreLabel, (900, 40))
    # Update the Pygame display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
