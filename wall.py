from figure import Figure
from line import Line
from pos import Pos


class Wall(Figure):
    def __init__(self, right, bottom, sym):
        super().__init__()

        self.values.append(Line(Pos(0, 0), Pos(right, 0), sym))
        self.values.append(Line(Pos(right - 1, 0), Pos(right - 1, bottom), sym))
        self.values.append(Line(Pos(0, bottom - 1), Pos(right, bottom - 1), sym))
        self.values.append(Line(Pos(0, 0), Pos(0, bottom), sym))
