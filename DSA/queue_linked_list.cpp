#include <iostream>
using namespace std;

struct Node {
  int data;
  Node* next;
};

Node* front = nullptr;
Node* rear = nullptr;

void insert(int value) {
  Node* newNode = new (nothrow) Node;
  if (newNode == nullptr) {
    cout << "Queue Overflow! (Out of memory) Cannot insert " << value << endl;
    return;
  }
  newNode->data = value;
  newNode->next = nullptr;

  if (front == nullptr) {
    front = rear = newNode;
  } else {
    rear->next = newNode;
    rear = newNode;
  }
  cout << value << " inserted into the queue." << endl;
}

void del() {
  if (front == nullptr) {
    cout << "Queue Underflow! No elements to delete." << endl;
    return;
  }

  Node* temp = front;
  cout << temp->data << " deleted from the queue." << endl;
  front = front->next;

  if (front == nullptr) {
    rear = nullptr;
  }
  delete temp;
}

void display() {
  if (front == nullptr) {
    cout << "Queue is empty." << endl;
    return;
  }

  cout << "Queue elements (front to rear): ";
  Node* temp = front;
  while (temp != nullptr) {
    cout << temp->data << " ";
    temp = temp->next;
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
