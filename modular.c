#include <stdio.h>

typedef long long ll ;
ll potencia2(ll x, ll p, ll mod){
    long long aux ;
    if (p == 0)
        return 1%mod;
    else if (p % 2 == 0) {
        aux = (potencia2(x,p/2,mod))%mod;
        return (aux*aux)%mod; 
    } else {
        aux = (potencia2(x,(p-1)/2,mod))%mod;
    return (x*((aux*aux)%mod))%mod;
    }
}
                                                           
int main() {
    int testCase, i=1;
    ll  b,e,m, r, pot; 
    scanf("%d", &testCase);

    while(testCase>0) {
        scanf("%lld %lld %lld", &b, &e, &m);
        pot = potencia2(b, e, m);
        printf("%d. %lld\n", i, pot);
        testCase--;
        i++;
    }
}