def count(i,a):
    # base case
    if i > a:
        return
    
    count(i+1,a)
    print(i)

a = int(input("Enter a number that how many time u want to print : "))
count(1,a)