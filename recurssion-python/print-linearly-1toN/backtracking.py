def count(i,a):
    # base case
    if i < 1:
        return
    
    count(i-1,a) 
    print(i)

a = int(input("Enter a number that how many time u want to print : "))
count(a,a)