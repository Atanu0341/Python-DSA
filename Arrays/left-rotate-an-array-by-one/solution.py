from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    temp = arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    return arr

