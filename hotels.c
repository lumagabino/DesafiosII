#include <stdio.h>

int main() {
    int iniIndex=0;
    int soma = 0;
    int maior = 0;
    int n, m;

    scanf("%d %d", &n, &m);
    int values[n];

    for(int j=0;j<n;j++){
          scanf("%d", &values[j]);
    }

    for (int i=0; i<n; i++){
        if (soma+values[i]<m){
            soma += values[i];
        }
        else if(soma==m){
            maior = m;
        }
        else{
            if(soma>maior){
                maior=soma;
            }   
            while(soma+values[i]>m){
                soma -= values[iniIndex];
                iniIndex += 1;
            }  
            soma += values[i];
            if(soma>maior){
                maior=soma;
            } 
        }  
    }   
    printf("%d\n", maior);

    return 0;
}

