import numpy as np

def getUnit(vector: np.array):
    return vector / np.linalg.norm(vector)