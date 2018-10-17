# -*- coding: utf-8 -*-
#cifra de césar
def retornaIndice(elemento, lista):
	indice = 0
	for i in range(len(lista)):
		if elemento == lista[i]:
			indice = i
			break
	return indice
	
letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

testes = int(raw_input())

for i in range(testes):
	preCifra = ""
	
	posCifra = raw_input()
	
	deslocamento = int(raw_input())
	
	for j in range(len(posCifra)):
		
		if (retornaIndice(posCifra[j], letras) - deslocamento) > 25:
			
			preCifra += letras[(retornaIndice(posCifra[j], letras) - deslocamento) % 26]
		
		else:
			preCifra += letras[retornaIndice(posCifra[j], letras) - deslocamento]
	
	print preCifra
