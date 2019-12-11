#include <stdio.h>
#include <stdlib.h>

#define INF 1E9
#define MAX 1000
int m[MAX][MAX];
int s[MAX][MAX]; 
int b[10000];
int a[10000];

 struct dict{
    int number;
    int freq;
  };


int compare(const void *a,const void *b) {
    int *x = (int *) a;
    int *y = (int *) b;
    return *x - *y;
}

// int matrix_chain_td ( int i , int j ) { 
//     if (m[i][j] < INF) return m[i][j];
//     // base case
//     if (i == j) return m[i][j] = 0;
//     for (int k = i; k < j; ++k) {
//         int q = matrix_chain_td(i ,k) + matrix_chain_td(k+1,j ) + b[ i ]*b[k+1]*b[ j +1]; 
//         if (q<m[i][j]) {
//             m[i][j] = q; s[i][j]=k;
//         } 
//     }
//     return m[i][j]; 
// }


int main() {
    int testCase, n, m, i;
    struct dict dictA[10000];


    scanf("%d", &testCase);

    while(testCase>0) {
        scanf("%d %d", &n, &m);
        for(i=0; i<n; i++) {
            scanf("%d", &a[i]);
        }
        for(int j=0; j<n; j++) {
            scanf("%d", &b[j]);
        }
        qsort(a, n, sizeof(int), compare);
        qsort(b, m, sizeof(int), compare);

        for(i=0; i<n; i++) {
            if(a[i]==a[i+1]) {
                dictA.number = 
            }
            else {
                
            }
        }



        testCase--;
    }
}
