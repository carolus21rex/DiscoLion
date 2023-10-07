import arcade

class MainMenu(arcade.View):
    def on_show_view(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        arcade.draw_rectangle_filled(400, 300, 400, 400, arcade.color.WHITE)

        # Draw the Start game text
        # text, x, y, color, size
        arcade.draw_text("START GAME", 350, 350, arcade.color.BLACK, 20)

        # Draw the Leaderboard text
        # text, x, y, color, size
        arcade.draw_text("LEADERBOARD", 350, 300, arcade.color.BLACK, 20)

        # Draw Settings text
        # text, x, y, color, size
        arcade.draw_text("SETTINGS", 350, 250, arcade.color.BLACK, 20)

        # Draw Quit text
        # text, x, y, color, size
        arcade.draw_text("QUIT", 350, 200, arcade.color.BLACK, 20)

    def on_mouse_press(self, x, y, button, modifiers):
        
        # Check if the mouse click is within the "START GAME" text area
        if 300 <= x <= 450 and 335 <= y <= 365:
            print("START")

        # Check if the mouse click is within the Leaderboard text area
        elif 300 <= x <= 450 and 285 <= y <= 315:
            print("LEADERBOARD")
            leaderboard_view = Leaderboard()
            self.window.show_view(leaderboard_view)     

        # Check if the mouse click is within the Settings text area
        elif 300 <= x <= 450 and 235 <= y <= 265:
            print("SETTINGS")
            settings_view = Settings()
            self.window.show_view(settings_view)

        # Check if the mouse click is within the Quit text area
        elif 300 <= x <= 450 and 185 <= y <= 215:
            arcade.close_window()


class Leaderboard(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RED)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.texture = arcade.load_texture("back_arrow.png")

        # This is the back button
        arcade.draw_rectangle_filled(60, 550, 75, 50, arcade.color.PURPLE)
        scale_factor = 0.1
        arcade.draw_texture_rectangle(60, 550, self.texture.width * scale_factor, self.texture.height * scale_factor, self.texture)

        arcade.draw_rectangle_filled(400, 300, 400, 400, arcade.color.WHITE)
        arcade.draw_text("LEADERBOARD", 350, 350, arcade.color.BLACK, 20)

    def on_mouse_press(self, x, y, button, modifiers):
        if 22.5 <= x <= 97.5 and 525 <= y <= 575:
            main_view = MainMenu()
            self.window.show_view(main_view)  

        

class Settings(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        arcade.draw_rectangle_filled(400, 300, 400, 400, arcade.color.WHITE)
        arcade.draw_text("SETTINGS", 350, 350, arcade.color.BLACK, 20)

class MyWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.x = 100
        self.y = 100

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y


def main():
     #Create an title window with a specified width and height
     window = MyWindow(800, 600, "Gigi's Game")
     menu_view = MainMenu()
     window.show_view(menu_view)
     arcade.run()

main()

