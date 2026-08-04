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
    int stack[n];
    int top = -1;
    stack[++top] = 0;
    stack[++top] = n - 1;
    while (top >= 0) {
        int h = stack[top--];
        int l = stack[top--];
        int pivot = arr[h];
        int i = l - 1;
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;
        int p = i + 1;
        for (int x = 0; x < n; x++) {
            cout << arr[x] << " ";
        }
        cout << endl;
        if (p - 1 > l) {
            stack[++top] = l;
            stack[++top] = p - 1;
        }
        if (p + 1 < h) {
            stack[++top] = p + 1;
            stack[++top] = h;
        }
    }
    return 0;
}
