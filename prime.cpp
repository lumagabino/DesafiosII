#include <stdio.h>
#include <math.h> 
#include <iostream>


bool * generatePrimes(int n){
    int i,j,k;
    int nSqrt = sqrt(n);
    bool array[nSqrt] = { 1 };

    for(int i=0; i<nSqrt; i++) {
        if(array[i]) {
            j = pow(i,i);
            k=0;
            while(j < n) {
                array[j] = 0;
                k+=1;
                j+=k*i;
            }
        }
    }
    return array;
}

int main() {
    int n;
    bool *listPrime;
    
    cin >> n;

    listPrime = generatePrimes(n);

    return 0;
}