#include <iostream>
using namespace std;

class Calculator
{
    public :

    int a,b;

    void sum()
    {
        cout << "Sum of the numebrs is : " << (a+b);
    }
};

int main()
{
    Calculator c;
    c.a = 4;
    c.b = 7;
    c.sum();
    return 0;
}