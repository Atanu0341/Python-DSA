#include <bits/stdc++.h> 

// Function to reverse a vector
vector<int> reverse(vector<int> v){
    int start = 0;
    int end = v.size() - 1;

    // Swap elements from start to end until start becomes greater than or equal to end
    while(start < end){
        swap(v[start++], v[end--]); // Increment start and decrement end simultaneously
    }
    return v; // Return the reversed vector
}

// Function to find the sum of two arrays represented by vectors
vector<int> findArraySum(vector<int>& a, int n, vector<int>& b, int m) {
    // Initialize variables and the result vector
    int i = n - 1; // Index for the last element of array a
    int j = m - 1; // Index for the last element of array b
    vector<int> ans; // Vector to store the sum of arrays
    int carry = 0; // Variable to store carry during addition

    // Add corresponding elements of a and b, along with carry, until both arrays are exhausted
    while(i >= 0 && j >= 0){
        int value1 = a[i]; // Get the current element from array a
        int value2 = b[j]; // Get the current element from array b

        int sum = value1 + value2 + carry; // Calculate the sum of current elements and carry
        carry = sum / 10; // Calculate the new carry
        sum = sum % 10; // Calculate the new sum after removing carry

        ans.push_back(sum); // Store the sum in the result vector

        i--; // Move to the previous element in array a
        j--; // Move to the previous element in array b
    }

    // Handle remaining elements in array a
    while(i >= 0){
        int sum = a[i] + carry; // Add the current element of array a and carry
        carry = sum / 10; // Calculate the new carry
        sum = sum % 10; // Calculate the new sum after removing carry

        ans.push_back(sum); // Store the sum in the result vector

        i--; // Move to the previous element in array a
    }

    // Handle remaining elements in array b
    while(j >= 0){
        int sum = b[j] + carry; // Add the current element of array b and carry
        carry = sum / 10; // Calculate the new carry
        sum = sum % 10; // Calculate the new sum after removing carry

        ans.push_back(sum); // Store the sum in the result vector

        j--; // Move to the previous element in array b
    }

    // Handle the case where carry is not zero after both arrays are exhausted
    while(carry != 0){
        int sum = carry; // Set sum to carry
        carry = sum / 10; // Calculate the new carry
        sum = sum % 10; // Calculate the new sum after removing carry

        ans.push_back(sum); // Store the sum in the result vector
    }

    // Reverse the result vector and return
    return reverse(ans);
}
