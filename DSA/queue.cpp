#include <iostream>
using namespace std;

#define MAX 5

int queue[MAX];
int front = -1;
int rear = -1;

void insert(int value) {
  if (rear == MAX - 1) {
    cout << "Queue Overflow! Cannot insert " << value << endl;
    return;
  }
  if (front == -1) {
    front = 0;
  }
  queue[++rear] = value;
  cout << value << " inserted into the queue." << endl;
}

void del() {
  if (front == -1 || front > rear) {
    cout << "Queue Underflow! No elements to delete." << endl;
    return;
  }
  cout << queue[front++] << " deleted from the queue." << endl;
  if (front > rear) {
    front = -1;
    rear = -1;
  }
}

void display() {
  if (front == -1) {
    cout << "Queue is empty." << endl;
    return;
  }
  cout << "Queue elements (front to rear): ";
  for (int i = front; i <= rear; i++) {
    cout << queue[i] << " ";
  }
  cout << endl;
}

int main() {
  int choice, value;

  while (true) {
    cout << "\nChoose the option:" << endl;
    cout << "1. Insert" << endl;
    cout << "2. Delete" << endl;
    cout << "3. Display" << endl;
    cout << "4. Exit" << endl;
    cout << "Enter your choice: ";
    cin >> choice;

    switch (choice) {
    case 1:
      cout << "Enter value to insert: ";
      cin >> value;
      insert(value);
      break;

    case 2:
      del();
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
