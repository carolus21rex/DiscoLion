import buildImage as BI
import backgroundConstruction as BC
import os


current_directory = os.getcwd()

def buildImage(background, overlay_path, x, y, xsize, ysize):
    return BI.buildImage(background, overlay_path, x, y, xsize, ysize)


def placeLion(img, x, y):
    return BC.place(img, os.path.join(current_directory, 'images', 'lion.png'), x, y, 200, 150)
