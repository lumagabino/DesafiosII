#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

int map(const int in)
{ return ((in & 2) ? '\x8a' - in : '\x95' - in); }

int main() {
    int t,n,k,i;
    
    cin >> t;
    for(k=0; k<t; k++){
        cin >> n;

        int arrX[n];
        int arrY[n];
        for(i=0; i<n; i++){
            cin >> arrX[i] >> arrY[i];
        }


   

    }

    cout << min << endl;
    return 0;
}