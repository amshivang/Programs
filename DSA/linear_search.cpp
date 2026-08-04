#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Enter the size of array: ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements in the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    int target;
    cout << "Enter the target: ";
    cin >> target;
    int i;
    for (i = 0; i < n; i++) {
        if (arr[i] == target) {
            break;
        }
    }
    if (i < n) {
        cout << "element found at index : " << i << endl;
    } else {
        cout << "element not found" << endl;
    }
    return 0;
}
