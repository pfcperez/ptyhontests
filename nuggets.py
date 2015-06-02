"""
Requerimientos del programa
1- Desplegar cuantos nuggets se necesitan para la fiestan o presionar q para salir
 Los paquetes esta divididos en las siguientes proporciones
6 pack
9 pack
20 pack

tines que seguir preguntando la cantidad de nuggets hasta que se presiones q

"""
def resta (total, numero):
	total = total - numero
	return total

def main ():
	paquete_treinta = 0
	paquete_nueve = 0
	paquete_seis = 0
	

	print('Cuantos nuggets necesitas? ')

	try:
		total_nuggets = int(raw_input('>>>  nuggets'))
	except:
		print('Error en nuggets')



	while (total_nuggets >0):
		#print total_nuggets
		
		if total_nuggets>=20:
			paquete_treinta+=1
			total_nuggets = resta(total_nuggets,20)
		elif total_nuggets >= 9 and total_nuggets < 20 :
			paquete_nueve += 1
			total_nuggets = resta(total_nuggets,9)
		elif total_nuggets <= 6 and total_nuggets < 9:
			paquete_seis += 1
			total_nuggets = resta(total_nuggets,6)


	
	#test = resta(total_nuggets,3)
	#print test
	print('Total de paquetes ')
	print('Paquetes de 20 = %s' %str(paquete_treinta))
	print('Paquetes de 9 = %s' %str(paquete_nueve))
	print('Paquetes de 6 = %s' %str(paquete_seis))
	print('Adios')

if __name__ == '__main__':
	main()
	



