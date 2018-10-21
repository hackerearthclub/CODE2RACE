#include <stdio.h>

int main(){
  int num, each, n1, n2, first, second, res;
  scanf("%d", &num);
  for (;num>0;num--){
    scanf("%d", &each);
    n1 = each / 2;
    n2 = each - n1;
    first = ((n2 * (n2 - 1)) * n1) / 2;
    second = (n1 * (n1 - 1) * (n1 - 2)) / 6;
    res = first + second;
    printf("%d\n", res);
  }
  return 0;
}
