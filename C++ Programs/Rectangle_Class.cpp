#include <iostream>
using namespace std;

class Rectangle
{
    public :

    int length, breadth;

    void display()
    {
        cout << "Length and Breadth of the Rectagle are : " << endl; 
        cout << length << endl;
        cout << breadth << endl;
    }
};

int main()
{
    Rectangle r;
    r.length = 78;
    r.breadth = 99;
    r.display();
}