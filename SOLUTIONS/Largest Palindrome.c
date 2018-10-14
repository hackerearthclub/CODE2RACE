#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  int cases, len, pal = 0, num, i;
  char n[10];
  scanf("%i", &cases);
  for (;cases!=0;cases--){
    scanf("%9s", n);
    for (len=0;n[len]!='\0';len++);
    num = atoi(n); // to decrease number
    while (pal == 0){ // while no palindrome keep searching
      sprintf(n, "%i", (num-1));
      for (i = 0; i<len/2;i++){ // check if number is palindrome, else break and other number
        if (n[len-1-i] == n[i]){ pal = 1 }
        else {
          pal = 0;
          break;
        }
      }
      num = atoi(n); // array to int to be able to decrease num
    }
    if (pal == 1){
      printf("%d\n", num);
      cases = len = pal = num = 0; // reinitialize everything so that results don't influence each other
    }
  }
}
