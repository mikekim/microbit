from microbit import *
import utime
import random

SCREEN_WIDTH = 5
SCREEN_HEIGHT = 5

# Eggs will be appearing on the top row and
# falling down, one row at a time, with every
# update (depending on speed).
# Player is needs to use buttons A and B to
# move the paddle left and right to catch
# falling eggs. Player gets a point for every egg
# they catch.
# If an egg falls and is not caught the game ends
# and final score is displayed.
# Shaking microbit restarts the game (only when
# it's game over).
class FallingEggs:
    def __init__(self):
        self.speed = 1  # line/second
        self.eggs = [[0]*SCREEN_WIDTH]*(SCREEN_HEIGHT-1)
        self.basket = Basket()
        self.score = 0
        self.last_update = utime.ticks_ms()
        self.is_game_over = False

    def update(self):
        self.basket.update()
        self.update_eggs()

    def update_eggs(self):
        if self.is_game_over:
            return
        # check time since last update, we should only update eggs
        # if sufficient time has passed.
        current_time = utime.ticks_ms()
        time_delta = current_time - self.last_update
        if time_delta < 1000 / self.speed:
            return

        self.move_eggs()
        self.add_new_egg()
        self.last_update = current_time

    
    def move_eggs(self):
        # Only eggs in last row are really interesting - we
        # need to check if they were caught or fell.
        for x, egg in enumerate(self.eggs[-1]):
            if not egg:  # "not egg" is the same as "egg == 0"
                # no egg here
                continue
            if x >= self.basket.x and x < self.basket.x + self.basket.width:
                self.score += 1
                if self.score % 3 == 0:
                    # increase speed every 3 points
                    self.speed += 0.2
            else:
                return self.game_over()

        # shift rows one down by removing the last one and inserting one
        # at the beginning.
        self.eggs = [[0]*SCREEN_WIDTH] + self.eggs[:-1]
        

    def game_over(self):
        # play sound too?
        self.is_game_over = True

    # New eggs will appear, one per line with probability 1/3 per second.
    def add_new_egg(self):
        if random.random() <= 0.3:
            # new egg appears! get its position.
            new_x = random.randrange(0, 4)
            self.eggs[0][new_x] = 9

    def draw(self):
        if self.is_game_over:
            display.show(self.score)
            return
        # convert eggs to image
        leds = self.eggs[:] + self.basket.leds()
        # image is a string of numbers with lines divided by colon, like:
        # boat = Image("05050:"
        #              "05050:"
        #              "05050:"
        #              "99999:"
        #              "09990")
        # we need to convert our list to such a string.
        display.show(Image(self.matrix_to_image_string(leds)))

    def matrix_to_image_string(self, matrix):
        string_rows = []
        for row in matrix:
            string_rows.append(self.row_to_image_string(row))
        return ":".join(string_rows)

    def row_to_image_string(self, row):
        return "".join([str(x) for x in row])


class Basket:
    def __init__(self):
        self.width = 2
        self.x = 1
        self.last_move = 0

    def update(self):
        current_time = utime.ticks_ms()
        if current_time - self.last_move < 110:
            return
            
        if button_a.is_pressed() and self.x > 0:
            self.x -= 1
            self.last_move = current_time

        if button_b.is_pressed() and self.x < SCREEN_WIDTH - self.width:
            self.x += 1
            self.last_move = current_time

    def leds(self):
        row = [0] * SCREEN_WIDTH
        for x in range(self.x, self.x + self.width):
            row[x] = 5
        return [row]


def main():
    game = FallingEggs()
    while True:
        if game.is_game_over and accelerometer.is_gesture('shake'):
            # New Game!
            game = FallingEggs()
        game.update()
        game.draw()

main()
