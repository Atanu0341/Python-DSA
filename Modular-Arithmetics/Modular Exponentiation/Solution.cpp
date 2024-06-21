#include <bits/stdc++.h>

// Function to compute (x^n) % m using modular exponentiation
int modularExponentiation(int x, int n, int m) {
    int result = 1;
    x %= m; // Ensure x is in the range [0, m)
    
    // Loop until n becomes 0
    while (n > 0) {
        // If n is odd, multiply result by x
        if (n & 1) {
            result = (1LL * result * x) % m;
        }
        
        // Square x for the next iteration
        x = (1LL * x * x) % m;
        
        // Reduce n by half (equivalent to n = n >> 1)
        n >>= 1;
    }
    
    // Return the final result
    return result;
}
