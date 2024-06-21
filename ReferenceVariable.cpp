#include<iostream>
using namespace std;

void update(int n){
    n++;
}

void update2(int& n){
    n++;
}

int& func (int a){
    int num = a;
    int& ans = num;
    return ans;
}

int* func(int n){
    int* ptr = &n;
    return ptr;
}

int main() {
    /*
    int i = 5;
    // create a ref variable
    int& j = i;

    cout<< i <<endl;
    i++;
    cout<< i <<endl;
    j++;
    cout<< i <<endl;
    cout<< j <<endl;
    */

   int n = 5;

   cout<<"befor value "<<n<<endl;
   update2(n);
   cout<<"after value "<<n<<endl;

   function(n);
   fun(n);

    return 0;
}