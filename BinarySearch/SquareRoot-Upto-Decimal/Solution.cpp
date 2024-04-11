#include <iostream>
using namespace std;

long long int sqrtInteger(int num){
        int start = 0;
        int end = num;
        long long int mid = start + (end-start)/2;
        int ans = -1;

        while(start<=end){

            long long int square = mid * mid;

            if(square == num){
                return mid;
            }

            else if(square < num){
                ans = mid;
                start = mid+ 1;
            }
            //sqaure>num
            else{
                end = mid - 1;
            }
            mid = start + (end-start)/2;
        }
        return ans;
    }
    
double morePrecision(int n, int precision, int tempSol){
    double factor = 1;
    double ans = tempSol;
    
    for (int i = 0 ; i<precision ; i++){
        factor = factor/10;
        // 0.1
        // 0.01
        // 0.001
        for (double j = ans ; j*j<n; j=j+factor){
            ans = j;
        }
    }
    return ans;
    
}

int main()
{

    int n;
    cout<<"Enter the number"<<endl;
    cin>>n;
    
    int tempSol = sqrtInteger(n);
    cout<<"Answer is "<< morePrecision(n, 3, tempSol) <<endl;
}