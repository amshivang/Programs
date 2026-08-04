#include <iostream>
using namespace std;

#define MAX 50

int stack[MAX];
int top = -1;

void push(int value) {
  if (top == MAX - 1) {
    cout << "Stack Overflow! Cannot push " << value << endl;
    return;
  }
  stack[++top] = value;
  cout << value << " pushed onto the stack." << endl;
}

void pop() {
  if (top == -1) {
    cout << "Stack Underflow! No elements to pop." << endl;
    return;
  }
  cout << stack[top--] << " popped from the stack." << endl;
}

void display() {
  if (top == -1) {
    cout << "Stack is empty." << endl;
    return;
  }
  cout << "Stack elements (top to bottom):" << endl;
  for (int i = top; i >= 0; i--) {
    cout << stack[i] << endl;
  }
}

int main() {
  int choice, value;

  while (true) {
    cout << "Choose the option:" << endl;
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
      push(value);
      break;

    case 2:
      pop();
      break;

    case 3:
      display();
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
