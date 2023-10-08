import buildImage as BI
import backgroundConstruction as BC
import buildTextImage as BTI
import optionsParser as OP
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

def question(img, question):
    return BC.place(img, BTI.text_to_png(question, 600, 150), 400, 0, 400, 200)

def answers(img, answers):
    j = 0
    for i in OP.answers(answers):
        img = BC.place(img, BTI.text_to_png(str(i), 100, 200), 550 + j * 50, 50, 80, 200)
        j += 1
    return img
