#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int is_prime(int num){
  if (num <= 1) return 0;
  if (num % 2 == 0 && num > 2) return 0;
  for(int i = 3; i < floor(sqrt(num)); i+= 2) if (num % i == 0) return 0;
  return 1;
}

int pandig(int num, int len){
  int arr[len], num_temp = num, k, invalid = 0, prime = 0, i, length = len;
  for (i=num;i>0;i--){
    if (i == 0) length = 1;
    length = floor (log10 (abs (i))) + 1;
    invalid = 0;
    k = 0;
    num_temp = i;
    for (int x=length-1; x>=0; x--) arr[x] = 0;
    for (;num_temp!=0;){
      k = num_temp % 10;
      if (k <= length && k!=0) arr[k-1] = 1;
      num_temp = num_temp/10;
    }
    for (int x=length-1;x>=0;x--){
      if (arr[x]!=1){
        invalid = 1;
      }
    }
    if (invalid == 0) prime = is_prime(i);
    if (prime == 1) break;
  }
  if (i == 0) return -1;
  return i;
}

int main(){
  int var, dig, iter;
  scanf("%d", &iter);
  for (;iter!=0;iter--){
    scanf("%d", &var);
    if (var == 0) dig = 1;
    else dig = floor (log10 (abs (var))) + 1;
    printf("%d\n", pandig(var, dig));
  }
}
