
#include <stdio.h>

int potencia(int n, int exp) {
    int i, pot;
    pot = n;
    for(i=1; i<exp; i++) {
        pot *= n;
    }
    return pot;
}

int totalDigitos(int n) {
    int i = 0;
    while(n != 0) {
        n = n/10;
        i++;
    }
    return i;
}

int main() {
    int testCase, n, number, numDig, aux;
    long long pot;
    scanf("%d", &testCase);
    
    while(testCase > 0) {
        
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
        
        testCase --;
    }
    
    return 0;
}
