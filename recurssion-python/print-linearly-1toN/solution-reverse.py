def count(i,a):
    # base case
    if i < 1:
        return
    
    print(i)
    count(i-1,a)

a = int(input("Enter a number that how many time u want to print : "))
count(a,a)