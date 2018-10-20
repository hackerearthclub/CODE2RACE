#include <stdio.h>
#include <stdlib.h>

int main (){

	int id,cont=0,soma=0;
	float med=0;

	printf("Informe sua idade: ");
	scanf("%d",&id);

	while(id!=0){
		++cont;
		soma = soma +id;
		med = (soma/cont);
		printf("Informe sua idade: ");
		scanf("%d",&id);

	}

	printf("A idade media do grupo é %.3f\n",med );



	return 0;
}