from tkinter import *


class Bubble:
    def __init__(self, x, y, width, height, color, text, canvas):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.canvas: Canvas = canvas
        self.draw()

    def draw(self):
        self.canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, outline=self.color,
                                fill=self.color)

        self.canvas.create_text(self.x + (self.width/2), self.y + (self.height/2), text=self.text, font="Times 14", justify=CENTER)
