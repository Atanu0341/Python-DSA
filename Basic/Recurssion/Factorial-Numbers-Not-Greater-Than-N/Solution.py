from typing import *

def fun(n,i,fac,result):
    if fac*i>n:
        return result
    fac*=i
    result.append(fac)
    return fun(n,i+1,fac,result)

def factorialNumbers(n: int) -> List[int]:
    return fun(n,2,1,[1])