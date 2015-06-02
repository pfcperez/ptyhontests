def totalporpersona(total, personas):
	try:
		totalporpagar = total / personas
	except:
		print('error en la funcion totalporpersona')
	return totalporpagar

def propina (total, personas, porcentaje):
	porcentaje = (porcentaje/100.00)
	print porcentaje
	try:
		tip = total * porcentaje
	except:
		print('Error en la funcion propina')
	return tip
def main ():

	print('La cuenta total es ?')
	while True:
		try:
			total = float(raw_input('>> '))
			break
		except:
			print('Numero no valido, intenta otro')

	print('Cuantas personas asistieron? ')
	while True:
		try:
			personas = int(raw_input('>>> ' ))
			break
		except:
			print('Error con el numerom de personas, escribe otro numero')

	print('Escribe el porcentaje de la propina')
	while True:
		try:
			tippercentaje = float(raw_input('<<<< %'))
			break
		except:
			print('Numero no valido')

	totalxpersona = totalporpersona(total,personas)
	propinaxpagar = propina(total,personas, tippercentaje)

	print('Total a pagar por persona sin propina es de %s' % str(totalxpersona))
	print('Total de propina por pagar %s' % str(propinaxpagar))

	totalmaspropina = total + propinaxpagar
	totalmaspropinamastip = float(totalmaspropina /personas)

	print('El total con propina es de %s' % str(totalmaspropina))
	print('El total a pagar por persona con propina %s' % str(totalmaspropinamastip))



if __name__ == '__main__':
	main()
	
		



