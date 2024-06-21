// Function to check if it is possible to allocate pages such that each student gets at most 'mid' pages
bool isPossible(vector<int> &arr, int n, int m, int mid) {
  // Initialize student count to 1 (at least one student will be assigned)
  int studentCount = 1;
  // Initialize page sum to 0 for the current student
  int pageSum = 0;

  // Iterate through each book
  for (int i = 0; i < n; i++) {
    // If adding the pages of the current book doesn't exceed 'mid'
    if (pageSum + arr[i] <= mid) {
      // Assign pages of the current book to the current student
      pageSum += arr[i];
    } else {
      // If adding the pages of the current book exceeds 'mid'
      // Move to the next student
      studentCount++;
      // If the number of students exceeds the limit 'm' or if the pages of the current book exceed 'mid'
      if (studentCount > m || arr[i] > mid) {
        // It's not possible to allocate pages in this way
        return false;
      }
      // Reset page sum for the new student
      pageSum = arr[i];
    }
  }
  // It's possible to allocate pages in this way
  return true;
}

// Function to find the minimum number of pages such that each student gets at most 'm' pages
int findPages(vector<int> &arr, int n, int m) {
  // Initialize start to 0
  int start = 0;

  // If the number of students exceeds the number of books, return -1 (not possible)
  if (m > n){
    return -1;
  }

  // Calculate the total number of pages in all books
  int sum = 0;
  for (int i : arr){
    sum += i;
  }

  // Initialize end to the total number of pages
  int end = sum;

  // Initialize the answer to -1 (if no solution found)
  int ans = -1;
  // Initialize mid using binary search
  int mid = start + (end - start) / 2;

  // Binary search loop
  while (start <= end) {
    // Check if it's possible to allocate pages with the current mid value
    if (isPossible(arr, n, m, mid)) {
      // Update answer and search in the left half
      ans = mid;
      end = mid - 1;
    } else {
      // If no solution found in the current mid, search in the right half
      start = mid + 1;
    }
    // Update mid for next iteration
    mid = start + (end - start) / 2;
  }
  // Return the minimum number of pages
  return ans;
}
