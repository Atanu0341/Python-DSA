from typing import List


# defining a recursive function
def fun(x,result):
    if x<1:#base condition
        return result
    result.append(x)
    return fun(x-1,result)
    
def printNos(x: int) -> List[int]:
    return fun(x,[])