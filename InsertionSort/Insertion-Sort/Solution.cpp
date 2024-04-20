#include <bits/stdc++.h>
using namespace std;

// Function to perform insertion sort on an array
void insertionSort(int n, vector<int> &arr) {
    // Traverse through all elements of the array
    for (int i = 1; i < n; i++) {
        // Store the current element to be inserted at its correct position
        int temp = arr[i];
        
        // Initialize a variable to traverse elements to the left of 'i'
        int j = i - 1;
        
        // Iterate through elements to the left of 'i' until the correct position for 'temp' is found
        for (; j >= 0; j--) {
            // If the current element is greater than 'temp', shift it to the right
            if (arr[j] > temp) {
                arr[j + 1] = arr[j]; // Shift operation
            } else {
                break; // If the current element is not greater than 'temp', break out of the loop
            }
        }
        
        // Insert 'temp' at its correct position in the sorted sequence
        arr[j + 1] = temp;
    }
}

int main() {
    // Example usage
    vector<int> arr = {12, 11, 13, 5, 6};
    int n = arr.size();

    insertionSort(n, arr);

    // Print sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
