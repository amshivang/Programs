#include <iostream>
using namespace std;

class Book
{ 
    public : 

    int price;

    void display()
    {
        cout << "Book Price: " << price << endl;
    }
};

int main() 
{
    Book b1;
    b1.price = 10;
    b1.display();
    return 0;
}