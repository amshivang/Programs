#include <iostream>
using namespace std;

class College
{
    public :

    string collegeName, Code;

    void display()
    {
        cout << "College name and it's code  : " << endl; 
        cout << collegeName << endl;
        cout << Code << endl;
    }
};

int main()
{
    College c;
    c.collegeName = "College of Engineering & Technology";
    c.Code = "CET";
    c.display();
}   