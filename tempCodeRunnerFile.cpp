#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, q, i, j, k, l, m, min;
    
    cin >> n;

    int arr[n];
    for(k=0; k<n; k++){
        cin >> arr[k];
    }
    
    cin >> q;
    for(l=0; l<q; l++) {
        cin >> i >> j;
        min = arr[i];
        for(m=i; m<=j; m++) {
            if(arr[m] < min) {
                min = arr[m];
            }
            cout << min << endl;
        }
    }
    return 0;
}