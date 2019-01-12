# include <stdio.h>
# include <stdlib.h>

int main (){

	float base, altura,area;

	printf("Informe a base do triangulo: ");
	scanf("%f",&base);
	printf("Informe a altura do triangulo");
	scanf("%f",&altura);

	while(altura<=0 || base<=0){
		if(altura<=0){
			printf("Altura invalida,favor informar um valor maior que 0: ");
			scanf("%f",&altura);
		}
		if(base<=0){
			printf("Base invalida,favor informar um valor maior que 0: ");
			scanf("%f",&base);

		}
	}

	area = (base*altura)/2;

	printf("A área do triangulo é: %f\n",area);


return 0;
}