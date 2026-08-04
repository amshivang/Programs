#include <iostream>
using namespace std;

class Account
{ 
    public : 

    int accountNumber;

    void display()
    {
        cout << "Account Number: " << accountNumber << endl;
    }
};

int main() 
{
    Account a1;
    a1.accountNumber = 10;
    a1.display();
    return 0;
}