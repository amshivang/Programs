#include <iostream>
using namespace std;

class Fact
{
    public:
    int factorial(int n)
    {
        if (n <= 1)
            return 1;
        return n * factorial(n - 1);
    }
};
int main()
{
    Fact f;
    int n;
    cout << "Enter a number : ";
    if (!(cin >> n) || n < 0) {
        cout << "Invalid input." << endl;
        return 1;
    }
    cout << f.factorial(n) << endl;
    return 0;
}