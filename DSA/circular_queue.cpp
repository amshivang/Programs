#include <iostream>
using namespace std;

#define MAX 5

int queue[MAX];
int front = -1;
int rear = -1;

void insert(int value) {
  if ((rear + 1) % MAX == front) {
    cout << "Queue Overflow! Cannot insert " << value << endl;
    return;
  }
  
  if (front == -1) {
    front = 0;
  }
  
  rear = (rear + 1) % MAX;
  queue[rear] = value;
  cout << value << " inserted into the circular queue." << endl;
}

void del() {
  if (front == -1) {
    cout << "Queue Underflow! No elements to delete." << endl;
    return;
  }
  
  cout << queue[front] << " deleted from the circular queue." << endl;
  
  if (front == rear) {
    front = -1;
    rear = -1;
  } else {
    front = (front + 1) % MAX;
  }
}

void display() {
  if (front == -1) {
    cout << "Queue is empty." << endl;
    return;
  }
  
  cout << "Queue elements: ";
  int i = front;
  while (true) {
    cout << queue[i] << " ";
    if (i == rear) {
      break;
    }
    i = (i + 1) % MAX;
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
    
    if (!(cin >> choice)) {
      cout << "Invalid input. Exiting." << endl;
      break;
    }

    switch (choice) {
      case 1:
        cout << "Enter value to insert: ";
        if (cin >> value) {
          insert(value);
        }
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
