def topo(lista):
	return pilha[0]
def removetopo(lista):
	del pilha[0]	
def base(lista):
	return pilha[-1]
def addbase(lista):
	pilha.append(pilha[0])	

#n = int(input()) #numero de cartas inseridas
#if n < 51:	#condicao do uri, max de cartas = 50
while True:
	n = int(input())
	if n == 0:
		break

	pilha = [] #instanciando a pilha
	i=1
	for i in range(n):     # adicionando os elementos a pilha
		pilha.append(i+1)	
	#print(pilha)
	descarte = ""
	while(len(pilha)>1):

		aux = topo(pilha)
		if len(pilha)== 2:
			descarte += str(aux)
		else:
			descarte += str(aux) + ", "  #variavel recebe os valores do topo		
		
		removetopo(pilha)#remove o elemento do topo da pilha
		addbase(pilha)		
		removetopo(pilha)			
		resto = str(topo(pilha))
	print("Discarded cards: %s"%descarte) #mostra a carta do topo						
		
	if topo(pilha) == base(pilha):

		print("Remaining card: %s"%resto)
		
		


