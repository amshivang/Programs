#include <iostream>
using namespace std;

class Marks 
{
    public :

    int a, b, c;

    void display()
    {
        cout << "Marks of three subjects are : " << endl; 
        cout << a << endl;
        cout << b << endl;
        cout << c << endl;
    }
};

int main()
{
    Marks m;
    m.a = 78;
    m.b = 99;
    m.c = 87;
    m.display();
}