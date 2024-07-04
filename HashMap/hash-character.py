def f(char, string):
    # Create a dictionary to count occurrences of each character in the string
    count_dict = {}

    for item in string:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    # Return the count of the specified character
    return count_dict.get(char, 0)

# Example usage with string = "abcdabejc"
string = "abcdabejc"
char = input("Enter a character to count: ")  # Let's say user inputs 'a'
print(f(char, string))  # Output will be 2, because 'a' occurs twice in the string
