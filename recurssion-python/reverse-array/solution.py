def f(a, l, r):
    if l >= r:
        return

    # Swap elements at indices l and r
    a[l], a[r] = a[r], a[l]

    # Recursive call
    f(a, l+1, r-1)

# Initialize the array
arr = [1, 3, 2, 5, 4]
n = len(arr)

# Call the function to reverse the array
f(arr, 0, n-1)

# Print the reversed array
print(arr)
