# functional

def f(s,i):

    if i>=n/2:
        return True
    
  
    if s[i] != s[n-i-1]:
        return False
    
    return f(s,i+1)

s = input("Enter a string :")
n=len(s)

if f(s,0) :
    print("Palindrome")
else:
    print("Not Palindrome")
