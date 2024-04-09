#include <bits/stdc++.h> 

int firstOccurrence(vector<int>& arr, int n, int k){
    int start = 0;
    int end = n-1;
    int ans = -1;

    int mid = start + (end - start)/2;

    while(start<=end){

        if(arr[mid] == k){
            ans = mid;
            end = mid - 1;
        }
        //go to the right side
        else if (k > arr[mid]){
            start = mid + 1;
        }
         //go to the left side where (k< arr[mid])
        else{
            end = mid - 1;
        }

         mid = start + (end - start)/2;
    }

    return ans;
}

int lastOccurrence(vector<int>& arr, int n, int k){
    int start = 0;
    int end = n-1;
    int ans = -1;

    int mid = start + (end - start)/2;

    while(start<=end){

        if(arr[mid] == k){
            ans = mid;
            start = mid + 1;
        }
        //go to the right side
        else if (k > arr[mid]){
            start = mid + 1;
        }
         //go to the left side where (k< arr[mid])
        else{
            end = mid - 1;
        }

         mid = start + (end - start)/2;
    }

    return ans;
}


pair<int, int> firstAndLastPosition(vector<int>& arr, int n, int k)
{
    pair<int, int> p;
    p.first = firstOccurrence(arr, n, k);
    p.second = lastOccurrence(arr, n, k);

    return p;
}