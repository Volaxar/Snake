class Point:
    def __init__(self,  x=0, y=0, sym='\0'):
        self.x = x
        self.y = y

        self.sym = sym

    def draw(self, terminal):
        terminal.put(self.x, self.y, self.sym)
