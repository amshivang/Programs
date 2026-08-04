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
    if (n > 0) {
        int highest = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > highest) {
                highest = arr[i];
            }
        }
        cout << highest << endl;
    }
    return 0;
}
