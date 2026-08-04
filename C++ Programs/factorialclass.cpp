#include <iostream>
using namespace std;

class Fact
{
    public:
    int n;
    int factorial()
    {
        if(n<1)
        return 1;
        return n * factorial(n-1);
    }
};
int main()
{
    Fact f;
    int n;
    cout << "Enter a number : ";
    cin >> n;
    cout << f.factorial(n);
}