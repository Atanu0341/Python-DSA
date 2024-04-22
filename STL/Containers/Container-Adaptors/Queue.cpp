// First in First Out
#include <iostream>
#include <queue>
using namespace std;

int main()
{

    queue<string> q;

    q.push("Data");
    q.push("Structure");
    q.push("Algorithm");

    cout << "First Element -> " << q.front() << endl;

    q.pop();
    cout << "Top Element -> " << q.front() << endl;

    cout << "Size of stack -> " << q.size() << endl;

    cout << "Empty or not -> " << q.empty() << endl;
}