#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isMultiple(int n){
    int result = 0, j, r, type = 0;
    
    j = n;
    
    while(j != 0){
        if(type){
            r = j % 10;
            result = result + r;
            j = j / 10;
            type = 0;
        }
        else{
            r = j % 10;
            result = result - r;
            j = j / 10;
            type = 1;
        }
    }
    return (abs(result));
}

int main() {
    int T;
    printf("Enter Number of testcases > ");
    scanf("%d", &T);
    int testcases[T];
    for (int i = 0; i<T; i++){
        printf("\nEnter testcase number %d > ",(i+1));
        scanf("%d",&testcases[i]);
    }
    for (int i = 0; i<T; i++){
        if(!isMultiple(testcases[i])){
            printf("\n1");
        }
        else{
            printf("\n0");
        }
    }
    return 0;
}

