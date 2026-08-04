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
    int low = 0;
    int high = n - 1;
    int mid;
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            break;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    if (low <= high) {
        cout << "element found at index : " << mid << endl;
    } else {
        cout << "element not found" << endl;
    }
    return 0;
}
