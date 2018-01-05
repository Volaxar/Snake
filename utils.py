from bearlibterminal.terminal import TK_LEFT, TK_UP, TK_RIGHT, TK_DOWN

from pos import Pos

FIELD_WIDTH = 80
FIELD_HEIGHT = 25

direction = {
    TK_LEFT: Pos(-1, 0),
    TK_UP: Pos(0, -1),
    TK_RIGHT: Pos(1, 0),
    TK_DOWN: Pos(0, 1)
}
