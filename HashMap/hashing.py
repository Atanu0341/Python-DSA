def f(num, arr):
    # Create a dictionary to count occurrences of each number in the array
    count_dict = {}

    for item in arr:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    # Return the count of the specified number
    return count_dict.get(num, 0)


# Example usage with arr = [1, 2, 1, 3, 2]
arr = [1, 2, 1, 3, 2]
num = int(input("Enter a number to count: "))  # Let's say user inputs 2
print(f(num, arr))  # Output will be 2, because 2 occurs twice in arr
