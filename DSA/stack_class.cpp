#include <iostream>
using namespace std;

class Stack {
public:
    int* arr;
    int max_size;
    int top;

    // Constructor to initialize stack with user-defined size
    Stack(int size) {
        max_size = size;
        arr = new int[max_size];
        top = -1;
    }

    // Destructor to clean up dynamically allocated array
    ~Stack() {
        delete[] arr;
    }

    void push(int value) {
        if (top == max_size - 1) {
            cout << "Stack Overflow! Cannot push " << value << endl;
            return;
        }
        arr[++top] = value;
        cout << value << " pushed onto the stack." << endl;
    }

    void pop() {
        if (top == -1) {
            cout << "Stack Underflow! No elements to pop." << endl;
            return;
        }
        cout << arr[top--] << " popped from the stack." << endl;
    }

    void display() {
        if (top == -1) {
            cout << "Stack is empty." << endl;
            return;
        }
        cout << "Stack elements (top to bottom):" << endl;
        for (int i = top; i >= 0; i--) {
            cout << arr[i] << endl;
        }
    }
};

int main() {
    int size;
    cout << "Enter the size of the stack: ";
    cin >> size;

    if (size <= 0) {
        cout << "Invalid stack size! Exiting." << endl;
        return 1;
    }

    Stack s(size);
    int choice, value;

    while (true) {
        cout << "\nChoose the option:" << endl;
        cout << "1. Push" << endl;
        cout << "2. Pop" << endl;
        cout << "3. Display" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value to push: ";
                cin >> value;
                s.push(value);
                break;

            case 2:
                s.pop();
                break;

            case 3:
                s.display();
                break;

            case 4:
                cout << "Exiting program." << endl;
                return 0;

            default:
                cout << "Invalid choice! Please try again." << endl;
                break;
        }
    }

    return 0;
}
