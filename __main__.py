from vfx.TkApp import TkApp
from vfx.parts import Table, Chart
import tkinter as tk
from tkinter import ttk
import time
import math


class App(TkApp):
    time = 0
    CANVAS_SIZE = 500, 500

    def _ready(self):
        self.root.title('MIZ')

        controls = tk.Frame(self.root)
        controls.pack(side=tk.RIGHT)

        self.beta_box = ttk.Spinbox(controls, from_=.1, to=.2, increment=.01)
        self.beta_box.set(0.1)
        self.beta_box.pack()

        self.canvas = tk.Canvas(width=self.CANVAS_SIZE[0], height=self.CANVAS_SIZE[1])
        self.canvas.pack()
        self.table = Table((10, 50, 492, 150), self.canvas)
        self.table.draw()

        self.chart = Chart(self.canvas, self.CANVAS_SIZE[0], self.CANVAS_SIZE[1] - self.table.cube.side * 2)
        self.chart.pos = self.CANVAS_SIZE[0] / 2, self.table.cube.side * 2
        self.chart.draw()
        self.fps_on_top = True

    def _physics_process(self, delta):
        self.table.update()
        self.chart.add_value(self.table.cube.pos[0] - self.CANVAS_SIZE[0] / 2, delta)
        self.time += delta
        x, y = self.table.cube.pos
        a = self.CANVAS_SIZE[0] / 2
        beta = float(self.beta_box.get())
        omega = 1
        t = self.time / 10
        self.table.cube.pos = a * math.exp(-beta * t) * math.cos(omega * t) + self.CANVAS_SIZE[0] / 2, y
        self.chart.update()


if __name__ == '__main__':
    app = App()
    app.run()
