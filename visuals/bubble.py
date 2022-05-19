from tkinter import *


class Bubble:
    def __init__(self, x, y, width, height, color, fontSize, text, canvas):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.fontSize = fontSize
        self.text = text
        self.canvas: Canvas = canvas
        self.draw()

    def draw(self):
        self.canvas.create_oval(self.x - (self.width/2), self.y - (self.height/2), self.x + (self.width/2), self.y + (self.height/2), outline=self.color,
                                fill=self.color)

        self.canvas.create_text(self.x, self.y, text=self.text, font=f"Times {self.fontSize}", justify=CENTER)
