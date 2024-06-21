def f(n):
    if n==0:
        return 0

    return n + f(n-1)

n = int(input("Enter the number : "))
print(f(n))