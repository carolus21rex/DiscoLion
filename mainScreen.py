import arcade

class MyWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        # Clear the screen and set the background color
        arcade.start_render()
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        #Draw the title box
        arcade.draw_rectangle_filled(400, 300, 400, 400, arcade.color.WHITE)


def main():
     #Create an title window with a specified width and height
     titleWin = MyWindow(800, 600, "Gigi's Game")

     arcade.run()

main()