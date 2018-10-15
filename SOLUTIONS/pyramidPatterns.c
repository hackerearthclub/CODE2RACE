#include <stdio.h>

void printHalfPyramid(int rowCount){
        for (int row = 1; row <= rowCount; row++) {
                for (int i = 1; i <= row; i++) {
                        printf("*");
                }
                printf("\n");
        }
}

void printPyramid(int rowCount){
        for (int row = 1; row <= rowCount; row++) {
                for (int i = 1; i <= rowCount*2-1; i++) {
                        if(i<=rowCount-row || i>=rowCount+row) printf(" ");
                        else printf("*");
                }
                printf("\n");
        }
}

void printInvertedPyramid(int rowCount){
        for (int row = rowCount; row >=1; row--) {
                for (int i = 1; i <= rowCount*2-1; i++) {
                        if(i<=rowCount-row || i>=rowCount+row) printf(" ");
                        else printf("*");
                }
                printf("\n");
        }
}


void printPascalTriangle(int rowCount){

        int pascalArray[rowCount][rowCount*2-1];
        for (int i = 0; i < rowCount; i++) {
                for(int j=0; j<=i; j++) {
                        if(j==0||j==i) {
                                pascalArray[i][j]=1;
                        }else{
                                pascalArray[i][j]=pascalArray[i-1][j-1]+pascalArray[i-1][j];
                        }
                }
        }

        for (int row = 1; row <= rowCount; row++) {
                for (int i = 1; i <= row; i++) {
                        printf("%d ",pascalArray[row-1][i-1]);
                }
                printf("\n");
        }
}

void floydsTriangle(int rowCount){
        int floyd=1;
        for (int row = 1; row <= rowCount; row++) {
                for (int i = 1; i <= row; i++) {
                        printf("%d ",floyd);
                        floyd++;
                }
                printf("\n");
        }
}

int main(int argc, char const *argv[]) {
        printf("printHalfPyramid(5)\n");
        printHalfPyramid(5);
        printf("printPyramid(5)\n");
        printPyramid(5);
        printf("printInvertedPyramid(5)\n");
        printInvertedPyramid(5);
        printf("printPascalTriangle(5)\n");
        printPascalTriangle(5);
        printf("floydsTriangle(5)\n");
        floydsTriangle(5);
        return 0;
}
