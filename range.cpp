#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, q, i, j, k, m, min;
    
    cin >> n;

    int arr[n];
    for(k=0; k<n; k++){
        cin >> arr[k];
    }
    
    cin >> q;
    for(int l=0; l<q; l++) {
        cin >> i >> j;
        min = arr[i];
        for(int l=i; l<=j; l++) {
            if(arr[l] < min) {
                min = arr[ml;
            }
            cout << min << endl;
        }
    }
    return 0;
}