import numpy as np

class ObjectData:
    def __init__(self, data, vector):
        self.data: list[dict] = data
        self.vector: np.array = vector
        
    def __str__(self):
     return f"<ObjectData data: {self.data}, vector: {self.vector}>"
 
    def __repr__(self):
        return f"<ObjectData data: {self.data}, vector: {self.vector}>"