#include <iostream>
using namespace std;

class Student
{
    static int count;
    
    public:
    void increase()
    {
        count++;
    }
    static void show()
    {
        cout << "Total Students = " << count;
    }
};

int Student::count=0;

int main()
{
    Student a,b,c;
    a.increase();
    b.increase();
    c.increase();

    Student::show();
}