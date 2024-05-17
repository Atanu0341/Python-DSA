#include <iostream>
using namespace std;

int main()
{

    // int n;
    // cin >> n;


    int row;
    cin>> row;

    int col;
    cin>>col;

    int **arr = new int *[row];
    // creation of 2d done
    for (int i = 0; i < row; i++)
    {
        arr[i] = new int[col];
    }

    // taking input
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin >> arr[i][j];
        }
    }

    cout<<endl;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << arr[i][j];
        }
        cout<<endl;
    }

    //releasing memory
    for (int i = 0; i < row; i++)
    {
        delete [] arr[i];
    }
    delete []arr;
    
    return 0;
}