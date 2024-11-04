# Python 1
Try out at https://python.microbit.org/v/3/

## 1. Display a single image

First, let's try to display an image. You already did that using block, let's try to do it with Python. Type in the following in your Python editor
```py
# ex1_image.py
from microbit import *

while True:
    display.show(Image.HEART)
```

Editor will automatically suggest other predefined images after you type in `Image.` Try with a few (you may already know some from previous lessons) and feel free to use your favorites.


## 2. Animation

Let's see if we can display a few images, one after another and get them to animate. Try the following code and see what happens:

```py
# ex2_animation.py
from microbit import *

while True:
    display.show(Image.HAPPY)
    sleep(300)
    display.show(Image.HEART)
    sleep(300)
    display.show(Image.CHESSBOARD)
    sleep(300)
```

Between displaying images we need to instruct microbit to wait a moment, otherwise it's too quick for our eyes to see that images are changing. To make it wait we use function `sleep` which takes a number of _milliseconds_ that it is supposed to wait before advancing to the next instruction.

_(Side question: how many milliseconds are there in a second?)_

### Try this

* What happens if you remove calls to "sleep" function? 
* We instructed it to sleep for 300ms (milliseconds) after displaying each image. Try with different values for `sleep`. Which ones work best in your opinion?
* What if you use different values for all of them?
* What if you use some very small or very large value?

## 3. "for" loop

Now, imagine we have a lot of images to display. Instead of writing the same code over and over to display and sleep let's try to use a list and loop over it using a "for" loop. Here's an example of a list and a loop.

```py
# ex3_for_loop.py 
from microbit import *

images = [Image.HEART, Image.CHESSBOARD, Image.SKULL]

while True:
    for image in images:
        display.show(image)
        sleep(400)
```

Can you explain what's happening here?

### Try this

* Try adding more images to the list (if you type in `Image.` editor will suggest you other predefined images).


## 4. Defining our own function

You call different predefined functions here all the time. "display.show" and "sleep" are both examples of "functions" - something we can do over and over and easily re-use. You can create your own custom functions too and share it with your friends for use in their programs. Try wrapping our animation in a function which we'll call every time a button is pressed. Try the following:

```py
# ex4_custom_function.py 
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
```

You should use functions every time you are re-using a piece of code. What functions would you like to do next?

## 5. Creating a custom image

So far we've been using predefined images. But you can also create your own. Try the following code to display a boat: 
```py
ex5_custom_image.py 
from microbit import *

boat = Image("00770:"
             "07770:"
             "00700:"
             "99999:"
             "09990")

while True:
    display.show(boat)
```



Try creating your own image by indicating a brightness of each LED, you can pick a number from 0 to 9 where zero means that given LED is turned off and completely dark to 9 which means that it is at its full brightness.



## 6. Something more?
You can find more tutorials on how to add movement, music and even use radio in microbit at
https://microbit-micropython.readthedocs.io/en/v2-docs/tutorials/introduction.html
