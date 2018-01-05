from figure import Figure
from point import Point
from utils import *


class Snake(Figure):

    def __init__(self, size=1, sym='*', vector=direction[TK_LEFT]):
        super().__init__()

        self.vector = vector
        self.sym = sym

        current_point = Point(FIELD_WIDTH // 2, FIELD_HEIGHT // 2, self.sym)

        for step in range(size):
            self.values.append(Point(current_point))
            current_point += self.vector

    def move(self):
        tail = self.values.pop(0)
        head = self.values[-1]

        tail.clear()

        next_point = Point(head + self.vector, self.sym)
        next_point.draw()
        self.values.append(next_point)

    def eat(self, food):
        food.sym = self.sym
        food.draw()

        self.values.append(food)

    def change_direction(self, key):
        if key in direction:
            self.vector = direction[key]

    def collision(self, let):
        if hasattr(let, 'values'):
            for item in let.values:
                if self.collision(item):
                    return True
        else:
            head = self.values[-1]

            if (head + self.vector) == let:
                return True
