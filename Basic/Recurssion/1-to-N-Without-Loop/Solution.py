from typing import List

def printNos(x: int) -> List[int]: 
    if x <= 0:
        return []
    
    result = printNos(x - 1)  # Recursively call printNos with x-1
    
    result.append(x)  # Append current value of x to the result list
    
    return result