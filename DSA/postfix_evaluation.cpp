#include <iostream>
#include <string>

using namespace std;

#define MAX 100

int stack[MAX];
int top = -1;

void push(int value) {
    if (top == MAX - 1) {
        cout << "Stack Overflow! Cannot push " << value << endl;
        return;
    }
    stack[++top] = value;
}

int pop() {
    if (top == -1) {
        cout << "Stack Underflow! No elements to pop." << endl;
        return -1;
    }
    return stack[top--];
}

int evaluatePostfix(string exp) {
    for (int i = 0; i < exp.length(); i++) {
        char c = exp[i];
        
        if (c == ' ') {
            continue;
        }
        
        if (c >= '0' && c <= '9') {
            int num = 0;
            while (i < exp.length() && exp[i] >= '0' && exp[i] <= '9') {
                num = num * 10 + (exp[i] - '0');
                i++;
            }
            i--;
            push(num);
        }
        else if (c == '+' || c == '-' || c == '*' || c == '/') {
            int val2 = pop();
            int val1 = pop();
            
            switch (c) {
                case '+': push(val1 + val2); break;
                case '-': push(val1 - val2); break;
                case '*': push(val1 * val2); break;
                case '/': 
                    push(val1 / val2); 
                    break;
            }
        }
    }
    return pop();
}

int main() {
    string exp;
    cout << "Enter postfix expression (e.g., 3 5 6 + 6 7 3 / * - +): ";
    getline(cin, exp);

    int result = evaluatePostfix(exp);
    cout << "Result of evaluation: " << result << endl;

    return 0;
}
