from typing import List

def printNos(x: int) -> List[int]: 
    if x <= 0:
        return []
    
    result = printNos(x - 1)  # Recursively call printNos with x-1
    
    result.append(x)  # Append current value of x to the result list
    
    return result


#  Another Solution

from typing import List

def recursiveFunction(x: int, ans: List[int]) -> None:
    if x == 0:
        return

    # Call recursive function.
    recursiveFunction(x - 1, ans)

    # Insert element in the list.
    ans.append(x)

def printNos(x: int) -> List[int]: 
    # Declaring an empty list.
    ans = []

    # Calling recursive function.
    recursiveFunction(x, ans)

    return ans