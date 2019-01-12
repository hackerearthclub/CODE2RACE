# include <stdio.h>
# include <stdlib.h>

int main () {

	int p=0,cont=0,soma=0;

	while(cont<=50){
		++cont;
		++p;
		if(p%2==0){
			soma=soma+p;

		}
	}

	printf("A soma dos 50 primeiros nºs é %d\n",soma);


	return 0;
}