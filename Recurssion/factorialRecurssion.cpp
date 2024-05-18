#include <iostream>
using namespace std;

int factorial(int n)
{

    // base case
    if (n == 0)
        return 1;

    // int smaller = factorial(n-1);
    // int bigger = n * smaller;
    return n * factorial(n - 1);
}

int main()
{

    int n;
    cin >> n;

    int ans = factorial(n);

    cout << ans << endl;

    return 0;
}