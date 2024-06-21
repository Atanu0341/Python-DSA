#include <iostream>
using namespace std;

void printSum(int arr[][3], int row, int col)
{
    cout<< "Printing Sum ->" << endl;
    for (int row = 0; row < 3; row++)
    {
        int sum = 0;
        for (int col = 0; col < 3; col++)
        {
            sum += arr[row][col];
        }
        cout << sum << " ";
    }
}

int main()
{

    // create 2d array
    int arr[3][3];

    cout << "Enter the elements " << endl;

    // taking input -> row wise input
    for (int row = 0; row < 3; row++)
    {
        for (int col = 0; col < 3; col++)
        {
            cin >> arr[row][col];
        }
    }

    // print
    for (int row = 0; row < 3; row++)
    {
        for (int col = 0; col < 3; col++)
        {
            cout << arr[row][col] << " ";
        }
        cout << endl;
    }

    printSum(arr, 3, 3);
    
    return 0;
}