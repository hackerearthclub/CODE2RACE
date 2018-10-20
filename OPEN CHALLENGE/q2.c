#include <stdio.h>
#include <stdlib.h>

int main (){

	int cont, i;
	cont=1;
	i=1;
	while(cont<=5){
		if(i%3==0){
			++cont;
			printf(" %d\n ",i);
		}
	++i;
	}

		
	

	return 0;
}