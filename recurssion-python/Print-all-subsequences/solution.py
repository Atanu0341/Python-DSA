def subsequences(ind, arr, current, n):
    # base case
    if ind >= n:
        print(current)
        return

    # case of take
    current.append(arr[ind])
    subsequences(ind + 1, arr, current, n)
    current.pop()

    # case of not take
    subsequences(ind + 1, arr, current, n)

arr = [3,1,2]  # example array
n = len(arr)
current = []
subsequences(0, arr, current, n)
