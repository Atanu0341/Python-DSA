class Solution {
public:
    int fib(int n) {
        
        // Base case: if n is 0, the Fibonacci number is 0
        if (n == 0)
            return 0;

        // Base case: if n is 1, the Fibonacci number is 1
        if (n == 1)
            return 1;

        // Recursive case: the Fibonacci number is the sum of the two preceding ones
        int ans = fib(n-1) + fib(n-2);

        // Return the calculated Fibonacci number
        return ans;
    }
};
