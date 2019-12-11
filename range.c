#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, q, i, j, k, l, m, min;
    
    scanf("%d", &n);

    int arr[n];
    for(k=0; k<n; k++){
        scanf("%d", &arr[k]);
    }

    scanf("%d", &q);
    for(l=0; l<q; l++) {
        scanf("%d %d", &i, &j);
        min = arr[i];
        for(m=i; m<=j; m++) {
            if(arr[m] < min) {
                min = arr[m];
            }
        }
        printf("%d\n", min);
    }
    return 0;
}