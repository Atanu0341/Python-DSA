#include<iostream>
using namespace std;

int main(){

    int num = 5;

    cout<<num<<endl;

    // address of Operator - &

    cout<<"address of num is "<<&num<<endl;

    int *ptr = &num;

    cout<<"address is : "<<ptr<<endl;
    cout<<"value is : "<<*ptr<<endl;

    cout<<"Size of Interger is "<<sizeof(num)<<endl;
    cout<<"Size of pointer is "<<sizeof(ptr)<<endl;

    double d = 4.3;
    double *p2 = &d;

    cout<<"address is : "<<p2<<endl;
    cout<<"value is : "<<*p2<<endl;

    cout<<"Size of double is "<<sizeof(d)<<endl;
    cout<<"Size of pointer is "<<sizeof(p2)<<endl;

    // pointer to int is created, and pointing to some garbage address
    // int *p = 0;

    // cout<<*p<<endl;

    int i = 5;
    int *p = 0;

    p = &i;

    cout<<p<<endl;
    cout<<*p<<endl;

    int num1 = 10;
    int a = num1;
    a++;
    cout<<a<<endl;

    int *p1 = &num1;
    (*p1)++;
    cout<<num1<<endl;

    // important concept

    int b = 3;
    int*t = &b;
    // cout<<(*t)++<<endl;
    *t = *t +1 ;
    cout<<*t<<endl;
    cout<<"before t "<<t<<endl;
    t = t + 1;
    cout<<t<<endl;
    cout<<"after t "<<t<<endl;
    



    return 0;
}