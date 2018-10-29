#include<stdio.h>
void main(){

int s, d, n = 1;

printf("Enter the number:\n");
scanf("%d", &s);

d=s;

while(s>0){
  n = n*s;
  s--;
 }
 
 printf(" Factorial of %d is %d", d, n);
}
