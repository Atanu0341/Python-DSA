int binarySearch(int arr[], int start, int end, int key) {
    // base case: element not found
    if (start > end) {
        return -1;
    }

    int mid = start + (end - start) / 2;

    // element found
    if (arr[mid] == key) {
        return mid;
    }

    // search in the right half
    if (arr[mid] < key) {
        return binarySearch(arr, mid + 1, end, key);
    }
    // search in the left half
    else {
        return binarySearch(arr, start, mid - 1, key);
    }
}

int search(vector<int> &nums, int target) {
    int n = nums.size();
    // Convert vector to array for binarySearch function
    int* arr = nums.data();
    // Call the binarySearch function
   
    return binarySearch(arr, 0, n - 1, target);
}