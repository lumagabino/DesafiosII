#include <stdio.h>

void calculateSeq(long long maiorFibo, long long fibo) {
    long long f3, f4, f5;

    f3 = maiorFibo - fibo;
    f4 = fibo - f3;
    f5 = f3 - f4;

    printf("%lld %lld %lld\n", f5, f4, fibo);
}

int main() {
    long long n, testCase, fibo=0, maiorFibo=1;

    scanf("%lld", &testCase);
    while(testCase>0) {
        scanf("%lld", &n);

        maiorFibo = 1;
        fibo = 0;
        if(n>=8) {
            while(maiorFibo<n) {
                maiorFibo += fibo;
                fibo = maiorFibo - fibo;
            }  
            calculateSeq(maiorFibo, fibo);
        }
        else {
            printf("impossible\n");
        }
        
        testCase--;
    }  
}