class Spring:
    def __init__(self, left, right, turns, radius):
        """
        Args:
            left: левый край пружины
            right: правый край пружины
            turns: количество витков
            radius: радиус пружины (не проволоки)
        """
        self.__left = min(left, right)
        self.__right = max(left, right)
        self.turns = turns
        self.radius = radius
        self.normal_len = self.len

    def __x_coords(self):
        for i in range(self.turns * 2):
            yield self.left + self.turn_width / 2 * i

    @property
    def coords(self):
        return [(x, self.radius if no % 2 == 0 else -self.radius) for no, x in enumerate(self.__x_coords())]

    @property
    def len(self):
        return self.right - self.left

    @property
    def turn_width(self):
        return self.len / self.turns

    @property
    def right(self):
        return self.__right

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, new_value):
        if new_value <= self.right:
            self.__left = new_value
        else:
            self.__left, self.__right = self.__right, new_value

    @right.setter
    def right(self, new_value):
        if new_value >= self.left:
            self.__right = new_value
        else:
            self.__right, self.__left = self.__left, new_value
