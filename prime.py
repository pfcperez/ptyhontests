def find_1000_prime():
	current_number = 2
	count = 0
	while True:
		es_primo = is_prime(current_number)
		if es_primo:
			count += 1
		if count == 1000:
			return current_number
		else:
			current_number += 1


def is_prime(number):

	""" Funcion para determinar si un numero es primo 
		toma un argumento = number
		retorna falso o verdadero
	"""
	es_primo = True
	n = abs(number)
	if n == 2:
		es_primo = True
	elif n % 2 == 0 :
		es_primo = False
	else:
		for x in range(3, int(n**0.5)+1,2):
			if n % x == 0:
				es_primo = False
	return es_primo
def main ():
	print ('Numeros primos')
	print '='*40

	primos = find_1000_prime()
	if primos:
		print " "
		print 'The 1000th Prime Number is: %d' %int(primos)
	else:
		print 'Error ocurred'


if __name__ == '__main__':
	main()