#include <iostream>
using namespace std;

class Person
{ 
    public : 

    int age, salary;

    void display()
    {
        cout << "Age: " << age << endl;
        cout << "Salary: " << salary << endl;
    }
};

int main() 
{
    Person p1;
    p1.age = 25;
    p1.salary = 50000;
    p1.display();
    return 0;
}