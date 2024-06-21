#include <iostream>
using namespace std;

void print(int arr[], int start, int end){

    for(int i = start; i<=end; i++){
        cout<< arr[i] <<" ";
    }cout<<endl;
}

bool binarySearch(int arr[], int start, int end, int key)
{

    print(arr,start,end);

    // base case

    // element not found
    if (start > end)
    {
        return false;
    }

    int mid = start + (end - start) / 2;

    // element found
    if (arr[mid] == key)
    {
        return true;
    }


    if (arr[mid] < key)
    {
        return binarySearch(arr, mid + 1, end, key);
    }
    else
    {
        return binarySearch(arr, start, mid - 1, key);
    }
}

int main()
{

    int arr[6] = {2, 4, 6, 10, 14, 16};
    int size = 6;
    int key =  10;
    bool ans = binarySearch(arr, 0, 5, key);

    cout<<"Present or not "<<ans<<endl;


    return 0;
}