#include <iostream>
using namespace std;

class Mobile
{
    public :

    int Price;
    string model;

    void display()
    {
        cout << "Price and Model of the Mobile are : " << endl; 
        cout << Price << endl;
        cout << model << endl;
    }
};

int main()
{
    Mobile m;
    m.Price = 78;
    m.model = "Galaxy S26 Ultra";
    m.display();
}