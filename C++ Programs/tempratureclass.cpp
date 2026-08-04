#include <iostream> 
using namespace std; 
 
class Temperature { 
    int temp[7]; 
 
public: 
    void input() { 
        for(int i=0;i<7;i++) 
            cin >> temp[i]; 
    } 
 
    void highest() { 
        int max = temp[0]; 
 
        for(int i=1;i<7;i++) 
            if(temp[i] > max) 
                max = temp[i]; 
 
        cout << "Highest Temperature = " << max; 
    } 
}; 
 
int main() { 
    Temperature t; 
    t.input(); 
    t.highest(); 
}