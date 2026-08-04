#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Enter the size of array: ";
    cin >> n;
    int arr[n];
    int sum = 0;
    cout << "Enter the elements in the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        sum += arr[i];
    }
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << sum << endl;
    return 0;
}
