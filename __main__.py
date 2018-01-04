from bearlibterminal import terminal


def draw(x, y, sym):
    terminal.put(x, y, sym)


terminal.open()

x1 = 1
y1 = 3
sym1 = '*'

draw(x1, y1, sym1)

x2 = 4
y2 = 5
sym2 = '#'

draw(x2, y2, sym2)

terminal.refresh()

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
