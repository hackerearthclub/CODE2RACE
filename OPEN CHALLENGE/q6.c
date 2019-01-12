# include <stdio.h>

int main (){

	int num,cont,primo;

	printf("Informe um numero maior que 1: ");
	scanf("%d",&num);

	while(num<=1){
		printf("Informe um numero maior que 1: ");
		scanf("%d",&num);
    }

    primo=0;
    for(cont=1;cont<=num;cont++){
    	printf("%d\n",cont );  //teste pra ver o funcionamento do cont dentro do for
    	if(num%cont==0){
    		primo=primo+1;

     	}
    }
    if (primo==2){
    	printf("O numero %d é primo\n",num );
    }
   	else{
    	printf("O numero %d  NÃO é primo\n",num );
   	}

    

	return 0;
}