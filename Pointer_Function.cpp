#include<iostream>
using namespace std;

// void print(int *p){
//     cout<<p<<endl;
// }

// void update(int *p){

//     p = p + 1;
//     cout<<"inside"<<p<<endl;
//     *p = *p + 1;

// }

void getSum(int arr[], int n){

    cout<<sizeof(arr)<<endl;

    int sum = 0;
    for(int i = 0; i<n; i++){
        sum += arr[i];
    }

    return sum;
}

int main() {

    // int value = 5;
    // int *p = &value;

    // // print(p);
    // update(*p);

    int arr[6] = {1,2,3,4,5,8};

    cout<<getSum(arr+3,5)<<endl;

    return 0;
}