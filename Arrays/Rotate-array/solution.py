def reverse(arr,start,end):

    while(start<=end):

        arr[start],arr[end]=arr[end],arr[start]

        start+=1

        end-=1

 

def rotateArray(arr: list, k: int) -> list:

    n=len(arr)

    reverse(arr,0,k-1)

    reverse(arr,k,n-1)

    reverse(arr,0,n-1)

    return arr