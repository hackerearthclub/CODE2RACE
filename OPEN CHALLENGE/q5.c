# include <stdio.h>
# include <stdlib.h>

int main (){

	int num;
	float fat,soma,i;

	printf("Informe um numero maior que 1: ");
	scanf("%d",&num);

	while(num<=1){
		printf("Favor informar um valor maior que 1: ");
		scanf("%d",&num);
	}
	soma=1;
	fat=1;
	for (i=1; i <=num; i++)
	{
		fat=fat*i;
		soma = soma+(1/fat);
	}
	printf("%.1f\n",fat);
	printf("A expressão E = 1 + 1/1! + .. +1/n! vale: %.3f\n",soma);


	return 0;

}
