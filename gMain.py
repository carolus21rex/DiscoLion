import buildImage as BI
import backgroundConstruction as BC
import os


current_directory = os.getcwd()

def buildImage(background, overlay_path, x, y, xsize, ysize):
    return BI.buildImage(background, overlay_path, x, y, xsize, ysize)


def placeLion(img, x, y):
    return BC.place(img, os.path.join(current_directory, 'images', 'Disco.png'), x, y, 200, 150)


def placeGiGi(img, x, y):
    q = min(180, x)
    img = BC.place(img, os.path.join(current_directory, 'images', 'ohNoGigi.png'), int(1100 * q / 30) - 300, 200, 200, 200)
    return BC.place(img, os.path.join(current_directory, 'images', 'gigi.png'), x, y, 200, 300)
