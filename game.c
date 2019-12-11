//
//  game.c
//  desafiosProg
//
//  Created by Luma Gabino Vasconcelos on 03/08/19.
//  Copyright © 2019 Luma Gabino Vasconcelos. All rights reserved.
//

#include "game.h"

int main() {
    int n1, n2, k1, k2;
    scanf("%d %d %d %d", &n1, &n2, &k1, &k2);
    
    if(n1 > n2) {
        printf("First\n");
    }
    else {
        printf("Second\n");
    }
    
    return 0;
}
