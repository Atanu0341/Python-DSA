#include <iostream>
using namespace std;

// Function to find the pivot element in a rotated sorted array
int getPivot(int arr[], int n)
{
    // Initialize start and end pointers for binary search
    int start = 0;
    int end = n - 1;

    // Calculate the middle index
    int mid = start + (end - start) / 2;

    // Perform binary search to find the pivot
    while (start < end)
    {
        // If the middle element is greater than the first element
        if (arr[mid] > arr[0])
        {
            start = mid + 1; // Search in the right half
        }
        else
        {
            end = mid; // Search in the left half
        }

        // Recalculate the middle index
        mid = start + (end - start) / 2;
    }

    // Return the index of the pivot element
    return start;
}

int main()
{
    // Example usage
    int arr[5] = {8, 10, 17, 1, 3};
    cout << "Pivot is " << getPivot(arr, 5) << endl;

    return 0;
}
