from array import *
import numpy as np


array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

def searchInArrayLinear(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if value == array[i][j]:
                return "The value is at row: "+str(i)+" and column "+str(j)
    return "element is not in array"
    
print(array1)

array2 = np.delete(array1, 0, axis=0)

print(array2)
