from cProfile import label
from tkinter import *
from gatherer import gatherData

from visuals.bubble import Bubble


# IDEA: use the top 2 words as vectors with the major directions (with max vector values spanning most of the screen)
# and then the rest are vectors with random directions and strengths.
# Then, map the bubbles as such with different colours for each neighborhood.
# The size of the bubble should correspond to the number of responses too

def main():

    print(gatherData())

    ws = Tk()
    ws.title('Art Display')
    ws.geometry('1080x720')
    ws.config(bg='#345')

    canvas = Canvas(
        ws,
        width=1080,
        height=720,
        bg="#fff"
    )

    canvas.pack()

    bubble = Bubble(100, 100, 100, 100, "#fb0", "Test", canvas)
    bubble.draw()

    ws.mainloop()


if __name__ == "__main__":
    main()
