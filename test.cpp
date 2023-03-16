#include <iostream>
using namespace std;
int * foo() {
    int x[10];
    cout << x << endl;
    cout << x[0] << endl;
    x[0] = 1;
    cout << x << endl;
    cout << x[0] << endl;
    return x;
}
int main(){
    cout << foo();
}
