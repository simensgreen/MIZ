class Cube:
    def __init__(self, side):
        self._side = side

    @property
    def coords(self):
        return (-self._side / 2, -self._side / 2), (self._side / 2, self._side / 2)
