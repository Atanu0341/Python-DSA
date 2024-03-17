n=int(input())  
# taking n as a input 
## write your code !!
n_str = str(n)

if n_str == n_str[::-1]:
    print("true")
else:
    print("false")