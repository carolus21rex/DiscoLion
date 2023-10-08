import buildImage as BI
import backgroundConstruction as BC
import os


current_directory = os.getcwd()

def buildImage(background, overlay_path, x, y, xsize, ysize):
    return BI.buildImage(background, overlay_path, x, y, xsize, ysize)


def placeLion(img, x, y):
    return BC.place(img, os.path.join(current_directory, 'images', 'Disco.png'), x, y, 200, 150)


def placeGiGi(img, x, y):
    q = max(30, x)
    img = BC.place(img, os.path.join(current_directory, 'images', 'ohNoGigi.png'), 800 * q / 30, 200, 200, 200)
    return BC.place(img, os.path.join(current_directory, 'images', 'gigi.png'), x, y, 200, 300)
