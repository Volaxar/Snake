from bearlibterminal import terminal

from pos import Pos


class Point(Pos):
    def __init__(self, *args):
        x = 0
        y = 0
        sym = ' '

        if len(args) == 1:
            x = args[0].x
            y = args[0].y
            sym = args[0].sym

        elif len(args) == 2:
            x = args[0].x
            y = args[0].y
            sym = args[1]

        elif len(args) == 3:
            x, y, sym = args

        super().__init__(x, y)

        self.sym = sym

    def clear(self):
        self.sym = ' '
        self.draw()

    def draw(self):
        terminal.put(self.x, self.y, self.sym)
