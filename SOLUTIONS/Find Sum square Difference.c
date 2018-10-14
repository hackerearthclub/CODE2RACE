#include <stdio.h>
#define max(x, y) (((x) > (y)) ? (x) : (y))
#define min(x, y) (((x) < (y)) ? (x) : (y))

int main(){
  int cases, i, n, sum1, sum2;
  scanf("%i", &cases);
  for (;cases!=0;cases--){
    scanf("%i", &n);
    for (i=n;i!=0;sum1+=i, i--);
    for (i=n;i!=0;sum2+=i*i, i--);
    printf("%i\n", max(sum1*sum1, sum2)-min(sum1*sum1, sum2));
    sum1 = sum2 = 0;
  }
}
