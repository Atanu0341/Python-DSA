def f(n):

    if n == 0:
        return 1

    return n * f(n-1)

n = int(input("Enter a number : "))
print(f(n))

# tc = O(N)
# sc = O(N)