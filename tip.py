#requiremeents
#una funcion para divir el costo de total entre las personas 
#segunda funcion calcula la propina
#tercera la funcion main


def division(total, people):
	#round 
	try:
		totalpp = round (total/people, 2)
	except:
		print ('Error calulando total por persona')

	return totalpp

def tip_cal(total, people, porcentaje):
	try:
		tip = total * tip
		total += tippp
	except:
		print 'Error al procesar la propina funcion'
		

	return tip


def main ():

	print ('Cuanto es el total de la cuenta? ')
	while True:
		try:
			 totalaccount = float((raw_input('>> $'))
			 break

		except:
			  	print ('Escribe un numero ')

	print ('Cuantas personas son ?')
	try:
		people = int(raw_input('>>> People '))
	except:
		print('Escribe un numero valido')

	print ('Cuanto porcentaje se dejara? ')
	try:
		perctip = int(raw_input('>>> % '))
	except:
		print ('Numero no valido')

	totalpersona = division(totalaccount,people)

	propina = tip_cal(totalaccount, people, perctip)


	



if __name__ == '__main__':
	main()
