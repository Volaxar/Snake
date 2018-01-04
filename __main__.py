from bearlibterminal import terminal

from point import Point


terminal.open()
terminal.set('input.filter=[keyboard, close]')

p1 = Point()
p1.x = 1
p1.y = 3
p1.sym = '*'

p1.draw(terminal)

p2 = Point()
p2.x = 4
p2.y = 5
p2.sym = '#'

p2.draw(terminal)

terminal.refresh()
terminal.read()
terminal.close()
