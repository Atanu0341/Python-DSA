def subsequences(index, ds, s, sum, arr, n):
    # Base case: if we have considered all elements
    if index == n:
        # If the current sum equals the target sum, print the subsequence
        if s == sum:
            print(ds)
        return
    
    # Include the current element in the subsequence
    ds.append(arr[index])
    s += arr[index]
    # Recurse with the current element included
    subsequences(index + 1, ds, s, sum, arr, n)
    
    # Backtrack: remove the current element from the subsequence
    ds.pop()
    s -= arr[index]
    # Recurse without the current element
    subsequences(index + 1, ds, s, sum, arr, n)

# Input array and parameters
arr = [1, 2, 1,]
n = len(arr)
sum = 2
ds = []

# Start the recursion
subsequences(0, ds, 0, sum, arr, n)
