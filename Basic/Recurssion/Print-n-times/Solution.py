from  typing import *


# defining a recursive function
def fun(i,n,result):
    if i>n:#base condition
        return result
    result.append("Coding Ninjas")
    return fun(i+1,n,result)
    
def printNtimes(n: int) -> List[str]:
    return fun(1,n,[])