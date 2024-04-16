#include <bits/stdc++.h> // Include necessary header file for standard C++ libraries

void selectionSort(vector<int> &arr, int n) { // Define a function named selectionSort that takes a vector of integers and its size as input
  for (int i = 0; i < n - 1; i++) { // Iterate through the array from the beginning to the second-to-last element
    int minIndex = i; // Assume the current index is the index of the minimum element

    for (int j = i + 1; j < n; j++) { // Iterate through the array starting from the next element after i
      if (arr[j] < arr[minIndex]) // If the current element is smaller than the element at minIndex
        minIndex = j; // Update minIndex to the index of the current element
    }

    swap(arr[minIndex], arr[i]); // Swap the element at minIndex with the element at index i
  }
}
