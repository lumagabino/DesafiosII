#include <stdio.h>
#include <stdlib.h>

int count=0, min, max, interval;

void combinationUtil(int arr[], int data[], int start, int end,  
                     int index, int r); 

int sum(int arr[], int n) {  
    int sum = 0;  
    for (int i = 0; i < n; i++) {
        sum += arr[i]; 
    }     
    return sum;  
} 

void printCombination(int arr[], int n, int r) { 
    int data[r];  
    combinationUtil(arr, data, 0, n-1, 0, r); 
} 
  
//recursao
void combinationUtil(int arr[], int data[], int start, int end, 
                     int index, int r) { 
    if (index == r) { 
        //printa combinacoes
        // for (int j=0; j<r; j++) {
        //     printf("%d ", data[j]);
        // }    
        // printf("\n"); 
  
        if(sum(data, r) >= min &&  sum(data, r) <= max && data[r-1]-data[0] >= interval) {
            count++;
        }

        return; 
    } 
  
    for (int i=start; i<=end && end-i+1 >= r-index; i++) { 
        data[index] = arr[i]; 
        combinationUtil(arr, data, i+1, end, index+1, r); 
    } 
} 
  
int main() { 
    int *arr, n, i, r;
    scanf("%d %d %d %d",&n, &min, &max, &interval);
    r = n;

    arr=(int*)malloc(n*sizeof(int));
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    while(r>0) {
        printCombination(arr, n, r); 
        r--;
    }

     printf("%d\n", count);
    
} 