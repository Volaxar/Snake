from bearlibterminal import terminal

from point import Point


terminal.open()
terminal.set('input.filter=[keyboard, close]')

p1 = Point(1, 3, '*')
p1.draw(terminal)

p2 = Point(4, 5, '#')
p2.draw(terminal)

terminal.refresh()
terminal.read()
terminal.close()
