""""
Programa que muestre el top 20 de palabras en el text de alice.txt

palabra --- numero de veces repetida

Se utilizan un diccionario, la palabra es la clave y la veces que se repite es el valor.

Se sortea el diccionario de tal manera que los que tengan mas veces repetida se muestran primero

Para ordenar por repeticiones se utilizan lists y tuplas

"""

def nose(file):
	



f = open('alice.txt', 'rU')

diccionario = {}
lista = []

for line in f:
	words = line.split()
	#print words

	for w in words:
		w = w.lower()
		if w in diccionario:
			
			diccionario[w]+=1
#		print w
		else:
			
			diccionario[w]=1
	#break
#print diccionario




f.close()