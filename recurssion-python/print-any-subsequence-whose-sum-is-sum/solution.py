#  technique is to print one answer


def subsequences(index, ds, s, sum, arr, n) -> bool:
    if index == n:
        if s == sum:
            print(ds)
            return True
        return False
    
    ds.append(arr[index])
    s += arr[index]
    if subsequences(index + 1, ds, s, sum, arr, n):
        return True
    
    ds.pop()
    s -= arr[index]
    if subsequences(index + 1, ds, s, sum, arr, n):
        return True
    
    return False

# Input array and parameters
arr = [1, 2, 1]
n = len(arr)
sum = 2
ds = []

# Start the recursion
subsequences(0, ds, 0, sum, arr, n)
