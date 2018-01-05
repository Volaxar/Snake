import random

from bearlibterminal import terminal

from point import Point
from snake import Snake
from utils import *
from wall import Wall


def game_over():
    s = 'Game Over!'

    terminal.printf(FIELD_WIDTH // 2 - len(s) // 2, FIELD_HEIGHT // 2, s)
    terminal.refresh()


def food_creator(_snake):
    while True:
        x = random.randint(1, FIELD_WIDTH - 2)
        y = random.randint(1, FIELD_HEIGHT - 2)

        if not _snake.collision(Pos(x, y)):
            return Point(x, y, '$')


def main():
    terminal.open()
    terminal.set('input.filter=[keyboard, close]')

    wl = Wall(FIELD_WIDTH, FIELD_HEIGHT, '+')
    wl.draw()

    snk = Snake(size=4)
    snk.draw()

    food = food_creator(snk)
    food.draw()

    terminal.refresh()

    while terminal.peek() != terminal.TK_CLOSE:
        if terminal.has_input():
            snk.change_direction(terminal.read())

        if snk.collision(wl) or snk.collision(snk):
            break

        if snk.collision(food):
            snk.eat(food)

            food = food_creator(snk)
            food.draw()
        else:
            snk.move()

        terminal.refresh()
        terminal.delay(100)

    if not terminal.has_input():
        game_over()
        terminal.read()

    terminal.close()


if __name__ == '__main__':
    main()
