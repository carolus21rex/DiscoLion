import pygame
import pymunk
from PIL import Image
import sys
import os
import random
import time

# Add the path to the parent directory (which contains GraphicsEngine) to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ""))
sys.path.append(parent_dir)


import gMain as GE
import Giraffe_Attacks as GG

class Person:
    def __init__(self, name, score): 
        self.name = name
        self.score = score

    def display(self):
        print(f"Name: {self.name}, Score: {self.score}")

def main():
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 1024, 529
    LIGHT_BLUE = (173, 216, 230)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)


    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DISCO LION")

    # Create a linked list to store names
    input_text = ""

    # GiGi's Variables
    gigiIndex = 0
    gigiMove = 1
    lastTime = time.time_ns()
    

    # Create a flag to keep track of the current screen
    current_screen = "main"

    # Create texts
    font = pygame.font.Font(None, 36)
    startText = "START GAME"
    settingsText = "SETTINGS"
    leaderboardText = "LEADERBOARD"
    quitText = "QUIT"

    # Main game loop
    runningTwo = True
    while runningTwo:
 
        # Clear the screen
        screen.fill(WHITE)

        # Background of the window
        screen.fill(LIGHT_BLUE)

        # Calculate the position and size of the menu box
        rectWidth = 450
        rectHeight = 450
        rect_x = (WIDTH - rectWidth) // 2
        rect_y = (HEIGHT - rectHeight) // 2

        # Draws the rectangle to the screen
        pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rectWidth, rectHeight))

        # Render "start game" text
        startSurface = font.render(startText, True, (0,0,0))
        startRect = startSurface.get_rect()
        startRect.center = (WIDTH // 2, 250)
        screen.blit(startSurface, startRect)

        # Render "leaderboard" text
        leaderSurface = font.render(leaderboardText, True, (0,0,0))
        leaderRect = leaderSurface.get_rect()
        leaderRect.center = (WIDTH // 2, 300)
        screen.blit(leaderSurface, leaderRect)

        # Render "settings" text
        settingsSurface = font.render(settingsText, True, (0,0,0))
        settingsRect = settingsSurface.get_rect()
        settingsRect.center = (WIDTH // 2, 350)
        screen.blit(settingsSurface, settingsRect)

        # Render "quit" text
        quitSurface= font.render(quitText, True, (0,0,0))
        quitRect = quitSurface.get_rect()
        quitRect.center = (WIDTH // 2, 396.75)
        screen.blit(quitSurface, quitRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningTwo= False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "main":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if leaderRect.collidepoint(event.pos):
                            print("LEADERBOARD")
                            current_screen = "leaderboard"
                        elif startRect.collidepoint(event.pos):
                            print("START")
                            current_screen = "name"
                        elif settingsRect.collidepoint(event.pos):
                            print("SETTINGS")
                            current_screen = "settings"
                        elif quitRect.collidepoint(event.pos):
                            runningTwo = False


        # Back button dimensions
        rectWidth = 100
        rectHeight = 100
        rect_x = (WIDTH - rectWidth) // 2
        rect_y = (HEIGHT - rectHeight) // 2

        # Draw the appropriate screen
        if current_screen == "settings":
            screen.fill(WHITE)
            
            # Background of the window
            screen.fill(LIGHT_BLUE)

            # Draws the rectangle to the screen
            pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rectWidth, rectHeight))

            #Draw leave button
            leaveSettingsSurface = font.render("LEAVE", True, (0,0,0))
            leaveSettingsRect = leaveSettingsSurface.get_rect()
            leaveSettingsRect.center = (50, 25)
            screen.blit(leaveSettingsSurface, leaveSettingsRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if leaveSettingsRect.collidepoint(event.pos):
                        current_screen = "main"


        elif current_screen == "leaderboard":
            screen.fill(WHITE)

            screen.fill(LIGHT_BLUE)

            pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rectWidth, rectHeight))

            #Draw leave button
            leaveLeaderSurface = font.render("LEAVE", True, (0,0,0))
            leaveLeaderRect = leaveLeaderSurface.get_rect()
            leaveLeaderRect.center = (50, 25)
            screen.blit(leaveLeaderSurface, leaveLeaderRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runningTwo = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if leaveLeaderRect.collidepoint(event.pos):
                        current_screen = "main"
                        
        elif current_screen == "name":
            screen.fill(WHITE)

            screen.fill(LIGHT_BLUE)

            pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rectWidth, rectHeight))

            # Ask for user name
            nameText = "Type your name: "
            nameSurface = font.render(settingsText, True, (0,0,0))
            nameRect = nameSurface.get_rect()
            nameRect.center = (WIDTH // 2, 350)
            screen.blit(nameSurface, nameRect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        user_name = input_text
                        input_text = ""
                        current_screen = "game"
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        elif current_screen == "game":
            screen.fill(WHITE)

            # Game Variables
            nameOfGame = "Disco Lion Game"
            heightOfDropLimit = 200
            commonLength = 50
            groundHeight =10
            groundThickness = 10
            tickCount = 0
            global score
            score = 0
            groundCutoff = 300
            global rectCount
            rectCount = 1
            global sqrCount
            sqrCount = 1
            global triangleCount
            triangleCount = 1

            # Set up the Pygame window
            screen_width, screen_height = 1024, 529
            screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption(nameOfGame)


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
                global triangleCount
                if pos[1] > heightOfDropLimit:
                    print("Didn't spawn shape because it was too close to the ground")
                elif triangleCount <= 0:
                    print("Didn't spawn Triangle because you ran out of placeable triangles!")
                else:
                    triangleCount = triangleCount-1
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
                global rectCount 
                if pos[1] > heightOfDropLimit:
                    print("Didn't spawn shape because it was too close to the ground")
                elif rectCount<= 0:
                    print("Didn't spawn Rectangle because you ran out of placeable rectangles!")
                else:
                    rectCount = rectCount - 1
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
                global sqrCount
                if pos[1] > heightOfDropLimit:
                    print("Didn't spawn shape because it was too close to the ground")
                elif sqrCount <= 0:
                    print("Didn't spawn Square because you ran out of placeable squares!")
                else:
                    sqrCount = sqrCount - 1
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


            def deleteRandomShape():
                global score

                if len(rectangles) + len(squares) + len(triangles) == 0:
                    print("No shapes to delete")
                    return

                # Choose a random shape
                random_shape = random.choice(rectangles + squares + triangles)

                # Remove the shape's body and shape from the Pymunk space
                space.remove(random_shape.body, random_shape)

                # Remove the shape from the respective list
                if random_shape in rectangles:
                    rectangles.remove(random_shape)
                elif random_shape in squares:
                    squares.remove(random_shape)
                elif random_shape in triangles:
                    triangles.remove(random_shape)

                # Update the score
                score = len(squares) + len(rectangles) + len(triangles)
                print(f"Shape deleted. Score: {score}")
            # Main loop
            running = True
            clock = pygame.time.Clock()

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif score>=20:
                        print("You won in ", seconds)
                        running = False
                        current_screen = "main"
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if leaveRect.collidepoint(event.pos):
                            print("LEAVE")
                            current_screen = "main"
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
                #shape counters

                # Background image
                current_directory = os.getcwd()

                # Load the background image
                background_path = os.path.join(current_directory, 'images', 'savana.png')
                background = Image.open(background_path)
                composite_image = GE.placeLion(background, 800, 370)
                composite_image = GE.placeGiGi(composite_image, gigiIndex - 170, 270)
                # Convert the composite image to a Pygame surface
                bg = pygame.image.fromstring(composite_image.tobytes(), composite_image.size, composite_image.mode)


                # Clear the screen + background
                screen.fill([255, 255, 255])
                screen.blit(bg, (0, 0))

                #Timer drawing
                myFont = pygame.font.SysFont("Times New Roman", 18)
                timerStr = "Stopwatch: " + str(seconds)
                timerLabel = myFont.render(timerStr, seconds, (0,0,0))
                screen.blit(timerLabel, (900, 20))
                #Draw leave button
                leaveSurface = font.render("LEAVE", True, (0,0,0))
                leaveRect = leaveSurface.get_rect()
                leaveRect.center = (50, 25)
                screen.blit(leaveSurface, leaveRect)
                # Draw the ground
                pygame.draw.line(screen, (0, 0, 0), (groundCutoff, screen_height - groundHeight), (screen_width-groundCutoff, screen_height- groundHeight), groundThickness)
                # Draw drop limit
                pygame.draw.line(screen, (255, 0, 0), (0, heightOfDropLimit), (screen_width, heightOfDropLimit), 3)

                # Draw the shapes
                for circle in circles:
                    pygame.draw.circle(screen, (0, 0, 255), (int(circle.body.position.x), int(screen_height - circle.body.position.y)), int(circle.radius))
                for rect in rectangles:
                    vertices = [rect.body.local_to_world(v) for v in rect.get_vertices()]
                    # Convert vertices to screen coordinates

                    points = [(int(point.x), int(screen_height - point.y)) for point in vertices]
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
                if triangleCount==0 and sqrCount==0 and rectCount==0:
                    gigiMove = 1
                    if gigiIndex == 200:
                        gigiMove = 0




                    if (gigiMove == -1):
                        rectCount = 1
                        sqrCount = 1
                        triangleCount = 1
                    #for i in range(50):
                # Gigi move
                if gigiMove == 1:
                    if gigiIndex < 200:
                        gigiIndex += 1
                if gigiMove == 0:

                    # do quiz
                    print("bob")
                if gigiMove == -1:
                    if gigiIndex > 0:
                        gigiIndex += 1

                #Score Logic
                for shape in shapes_to_remove:
                    score=score-1
                    if shape in squares:
                        squares.remove(shape)
                    elif shape in rectangles:
                        rectangles.remove(shape)
                    elif shape in triangles:
                        triangles.remove(shape)
                    shapes_to_remove.remove(shape)
                    
                score = len(squares) + len(rectangles) + len(triangles)
                scoreStr = "Score: " + str(score)
                scoreLabel = myFont.render(scoreStr, score, (0,0,0))
                screen.blit(scoreLabel, (900, 40))

                

                # Update the Pygame display
                pygame.display.flip()
                clock.tick(60)

                            

        pygame.display.flip()

    pygame.quit()

main()