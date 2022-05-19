import math
from cProfile import label
from tkinter import *

import numpy as np
from coordinate import Coordinate

from gatherer import gatherData
from helper import addMissingWords, getAnswerVector, rgb_to_hex, sortDictByVal
from math_helper import getUnit
from object_data import ObjectData
from screen_converter import ScreenConverter
from visuals.bubble import Bubble

# IDEA: use the top 2 words as vectors with the major directions (with max vector values spanning most of the screen)
# and then the rest are vectors with random directions and strengths.
# Then, map the bubbles as such with different colours for each neighborhood.
# The size of the bubble should correspond to the number of responses too

WIDTH = 1440
HEIGHT = 900

MAX_SCALE = 2

BUBBLE_SIZE = 100


def main():
    tmpData = [
        {'Pretty': 10},
        {'Pretty': 2, 'Calming': 1},
        {'Pretty': 2, 'Calming': 1, 'Beautiful': 6},
        {'Calming': 10},
        {"Beautiful": 10},
        {"Gorgeous": 10},
        {"Amazing": 10},
        {"Amazing": 3, "Gorgeous": 1},
        {"Amazing": 3, "Gorgeous": 8},
    ]

    sortedData: list[dict] = addMissingWords(tmpData)
    # sortedData: list[dict] = addMissingWords(gatherData())
    vectorData: list[np.array] = [getAnswerVector(data) for data in sortedData]
    objectData = ObjectData(sortedData, vectorData)

    print(objectData)

    numDirections = len(list(sortedData[0].keys()))
    print(numDirections)

    radAngle = (math.pi*2)/numDirections
    print(radAngle)

    dirArr = [getUnit(np.array([math.cos(radAngle*i), math.sin(radAngle*i)]))
              for i in range(numDirections)]

    print("The following are the directions:", dirArr)

    projMatrix = np.array(dirArr)
    print(f"Projection Matrix: {projMatrix}")

    projectedObjectVectors = np.array(
        list(map(lambda v: np.matmul(v, projMatrix), objectData.vector)))
    projectedObjectVectors = getUnit(projectedObjectVectors)
    print("Projected object vectors:", projectedObjectVectors)

    projectedObjectData = ObjectData(objectData.data, projectedObjectVectors)

    ws = Tk()
    ws.title('Art Display')
    ws.geometry(f'{WIDTH}x{HEIGHT}')
    ws.config(bg='#345')

    canvas = Canvas(
        ws,
        width=WIDTH,
        height=HEIGHT,
        bg="#eee"
    )

    canvas.pack()

    screenConverter = ScreenConverter(WIDTH, HEIGHT)

    for i, vec in enumerate(projectedObjectData.vector):
        loc: Coordinate = screenConverter.convertVectorToScreenCoordinates(
            vec*MAX_SCALE)

        bubble = Bubble(loc.x, loc.y, BUBBLE_SIZE, BUBBLE_SIZE, rgb_to_hex(list(np.random.choice(range(50, 256), size=3))), 10,
                        projectedObjectData.data[i], canvas)
        bubble.draw()

    ws.mainloop()


if __name__ == "__main__":
    main()
