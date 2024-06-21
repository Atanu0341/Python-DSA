# def a():
#     print("Hello")
#     a()

# a()

def f(count=0):  # Initialize count as a parameter
    if count == 4:
        return
    print(count)
    count += 1
    f(count)  # Pass the updated count to the recursive call

f()  # Call the function to start the recursion
