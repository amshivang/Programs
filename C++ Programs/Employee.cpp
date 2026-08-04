#include <iostream>
using namespace std;

class Employee
{ 
    public : 

    int id;

    void display()
    {
        cout << "Employee ID: " << id << endl;
    }
};

int main() 
{
    Employee e1;
    e1.id = 10;
    e1.display();
    return 0;
}