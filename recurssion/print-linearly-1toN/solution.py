def count(i,a):
    # base case
    if i > a:
        return
    
    print(i)
    count(i+1,a)

a = int(input("Enter a number that how many time u want to print : "))
count(1,a)