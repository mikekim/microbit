from microbit import *

def animate():
    images = [Image.HEART, Image.CHESSBOARD, Image.SKULL]

    for image in images:
        display.show(image)
        sleep(400)

while True:
    if button_a.is_pressed():
        animate()
    display.clear()
