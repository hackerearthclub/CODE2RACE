#include<stdio.h>
int even(int n1);
int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
	   int num;
	   scanf("%d",&num);
	   even(num);
	}
	return 0;
}

int even(int n1){
       int a[n1];
       int count=0;
       for(int i=0;i<n1;i++){
		scanf("%d",&a[i]);
	}
    for(int i=0;i<n1;i++){
		if((a[i]%2)==0){
		count++;
	}
	}
       printf("%d",count);
	
	return 0;
}