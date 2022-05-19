import numpy as np

#Note: Returns objects with the same key order (MUST RUN Python 3.7+)
def addMissingWords(objList: list[dict]):
    res = []
    words = []
    for obj in objList:
        words.extend(list(obj.keys()))
        
    for obj in objList:
        newObj = {word: (obj[word] if word in obj else 0) for word in words}
        res.append(newObj)
    
    return res

# From https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
def sortDictByVal(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

def getAnswerVector(obj: dict) -> np.array:
    return np.array(list(obj.values()))

def rgb_to_hex(rgb):
  return f"#{int_to_hexstr(rgb[0])}{int_to_hexstr(rgb[1])}{int_to_hexstr(rgb[2])}"

def int_to_hexstr(val):
    return ('{:X}').format(val).zfill(2)