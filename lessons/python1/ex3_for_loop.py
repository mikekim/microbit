from microbit import *

images = [Image.HEART, Image.CHESSBOARD, Image.SKULL]

while True:
    for image in images:
        display.show(image)
        sleep(400)
