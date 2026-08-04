#include <iostream>
using namespace std;

class Student 
{ 
    public : 

    string name, course; 
    int age, rollnumber;

    void input()
    {
        cout << "Enter Name: ";
        getline(cin, name);
        cout << "Enter Coruse: ";
        getline(cin, course);
        cout << "Enter Age: ";
        cin >> age;
        cout << "Enter Roll Number: ";
        cin >> rollnumber;
    }

    void display()
    {
        cout << "Name: " << name << endl;
        cout << "Course: " << course << endl;
        cout << "Age: " << age << endl;
        cout << "Roll Number: " << rollnumber << endl;
    }
};

int main() 
{
    Student s;
    s.input();
    s.display();
    return 0;
}