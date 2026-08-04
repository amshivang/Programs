#include <iostream> 
using namespace std; 
 
class Marks { 
    int marks[5]; 
 
public: 
    void input() { 
        for(int i=0;i<5;i++) 
            cin >> marks[i]; 
    } 
 
    void average() { 
        int sum=0; 
        for(int i=0;i<5;i++) 
            sum += marks[i]; 
 
        cout << "Average = " << sum/5; 
    } 
}; 
 
int main() { 
    Marks m; 
    m.input(); 
    m.average(); 
}