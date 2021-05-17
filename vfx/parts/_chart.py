from vfx._drawable import Drawable


class Chart(Drawable):
    id = None
    x_factor = 1
    MAIN_LINE_SKIN = {'width': 3}

    def __init__(self, canvas, limit_x, limit_y):
        self.limit_x = limit_x
        self.canvas = canvas
        self.limit_y = limit_y
        self.planks_coords = []
        self.values = []
        self.delta = 0
        self.time = 0
        self.planks_step = 50
        self.planks_counter = 0

    def draw(self):
        self.delete()
        self.planks_coords = []
        for i in range(0, self.limit_y, self.planks_step):
            self.planks_coords.append((-self.limit_x / 2, i))
            self.planks_coords.append((self.limit_x / 2, i))
        if len(self.values) > 1:
            self.id = self.canvas.create_line(self.values, **self.MAIN_LINE_SKIN, tags=(self,))
        for plank in self.separate_planks():
            self.canvas.create_line(self.add_pos(plank), tags=(self, 'plank'))
        self.canvas.create_line(self.add_pos(((0, 0), (0, self.limit_y))))

    def update(self):
        if self.id:
            self.canvas.coords(self.id, self.flatten(self.add_pos(self.values)))
            self.delete_planks()
            self.draw_planks()
        else:
            self.draw()

    def draw_planks(self):
        for plank in self.separate_planks():
            self.canvas.create_line(self.add_pos(plank), tags=('plank', self), dash=(1,))

    def separate_planks(self):
        for i in range(0, len(self.planks_coords) - 1, 2):
            yield self.planks_coords[i], self.planks_coords[i + 1]

    def delete_planks(self):
        self.canvas.delete('plank')

    def move_all(self, delta):
        self.values = list(filter(lambda val: 0 <= val[1] <= self.limit_y, [(x, y - delta) for x, y in self.values]))
        last_plank_0 = self.planks_coords[-2]
        last_plank_1 = self.planks_coords[-1]
        self.planks_coords.append((last_plank_0[0], last_plank_0[1] + self.planks_step))
        self.planks_coords.append((last_plank_1[0], last_plank_1[1] + self.planks_step))
        self.planks_coords = list(filter(lambda val: 0 <= val[1] <= self.limit_y, [(x, y - delta) for x, y in self.planks_coords]))

    def delete(self):
        self.canvas.delete(self)

    def add_value(self, value, delta):
        self.time += delta
        y_pos = self.time
        if self.time > self.limit_y:
            y_pos = self.limit_y
            self.move_all(delta)
        if abs(value * 2) > self.limit_x:
            self.x_factor = self.limit_x / abs(value * 2)
            self.values = [(x * self.x_factor, y) for x, y in self.values]
        self.values.append((value * self.x_factor, y_pos))
        self.canvas.delete('mark')
        self.canvas.create_line(self.add_pos(((value * self.x_factor, -20), (value * self.x_factor, y_pos))),
                                width=1, fill='red', tags=('mark', self))
