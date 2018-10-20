#include <stdio.h>

int sumoffactdigits(int n){
  int m=1,temp=0,x,j,sum=0,d;
  int arr[7000];
  arr[1]=1;
  for(x=1;x<=n;x++){
    for(j=1;j<=m;j++){
      d=arr[j]*x+temp;
      arr[j]=d%10;
      temp=d/10;
    }
    while(temp!=0){
      m=m+1;
      arr[m]=temp%10;
      temp/=10;
    }
  }
  for(x=m;x>=1;x--){
    sum+=arr[x];
  }
  return sum;
}

int main(){
  int count, num;
  scanf("%d", &count);
  for (;count!=0;count--){
    scanf("%d", &num);
    printf("%d\n", sumoffactdigits(num));
  }
  return 0;
}
