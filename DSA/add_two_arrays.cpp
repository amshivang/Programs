#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cout << "Enter the size of array: ";
    if (!(cin >> n) || n <= 0) {
        return 0;
    }
    vector<int> arr1(n);
    vector<int> arr2(n);
    cout << "Enter the elements in the first array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr1[i];
    }
    cout << "Enter the elements in the second array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr2[i];
    }
    for (int i = 0; i < n; i++) {
        cout << arr1[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
    vector<int> arr3(n);
    for (int i = 0; i < n; i++) {
        arr3[i] = arr1[i] + arr2[i];
    }
    for (int i = 0; i < n; i++) {
        cout << arr3[i] << " ";
    }
    cout << endl;
    return 0;
}
