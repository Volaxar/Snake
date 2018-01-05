class Figure:

    def __init__(self):
        self.values = []

    def draw(self):
        for item in self.values:
            item.draw()
