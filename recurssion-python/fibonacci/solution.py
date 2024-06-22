# Multiple recursion

def f(n):
    #  base case

    if n<=1:
        return n
    
    return f(n-1)+f(n-2)

n=int(input("Enter number : "))

print(f(n))

#  TC : (2n) exponential in nature