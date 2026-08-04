#include <iostream>
using namespace std;

    class Largest
    {
        public :
        int a,b,c;
        void input()
        {
        cout << "Enter three numbers : " << endl;
        cin >> a;
        cin >> b;
        cin >> c;
        }
        void lar()
        {
            if(a > b && a > c)
            cout << a << " is largest";
            else if(b > a && b > c)
            cout << b << " is largest";
            else 
            cout << c << " is largest";
        }
    };

    int main(){
        Largest l;
        l.input();
        l.lar();
    }