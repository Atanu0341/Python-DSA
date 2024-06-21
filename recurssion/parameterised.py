def f(i,sum):
    if i<1:
        print(sum)
        return

    f(i-1,sum+i)

n = int(input("Enter number: "))
f(n,0)