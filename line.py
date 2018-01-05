from figure import Figure
from point import Point
from pos import Pos


class Line(Figure):
    def __init__(self, from_p, end_p, sym):
        super().__init__()

        vector = Pos(int(bool(end_p.x - from_p.x)), int(bool(end_p.y - from_p.y)))

        while from_p != end_p:
            self.values.append(Point(from_p.x, from_p.y, sym))
            from_p += vector
