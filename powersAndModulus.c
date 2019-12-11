#include <stdio.h>

int potencia(int n, int exp) {
    int i, pot;
    pot = n;
    for(i=1; i<exp; i++) {
        pot *= n;
    }
    return pot;
}

int main() {
    int b, aux;
    long long pot, a;

    scanf("%d", &n);
    number = n;
    numDig = totalDigitos(n);
    
    pot = 0;
    while(n != 0) {
        aux = n%10;
        pot = pot + potencia(aux, numDig);
        n = n/10;
    }
    
    
    if(pot == number) {
        printf("Armstrong\n");
    }
    else {
        printf("Not Armstrong\n");
    }

    
    return 0;
}