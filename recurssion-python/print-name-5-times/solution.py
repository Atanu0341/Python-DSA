def name(i,a):
    # base case
    if i>a:
        return

    print("atanu")
    name(i+1,a)



a = int(input("Enter number of times you want name should print : "))
name(1, a)