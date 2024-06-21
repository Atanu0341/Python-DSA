#include<iostream>
using namespace std;

void reachHome(int step, int destination){

    cout<<"steps "<<step <<" destination "<<destination<<endl;
    // base case
    if(step == destination){
        cout<<"Reached Home"<<endl;
        return;
    }

    // processing
    step++;
    // recursive call
    reachHome(step, destination);

}


int main() {

    int destination = 10;
    int step = 1;

    cout<<endl;

    reachHome(step, destination);

    return 0;
}