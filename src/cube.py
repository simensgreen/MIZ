class Cube:
    def __init__(self, side):
        self.side = side

    @property
    def coords(self):
        return (-self.side / 2, -self.side / 2), (self.side / 2, self.side / 2)
