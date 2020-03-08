from lxml import etree
pokemon = etree.parse('pokemon.xml')
from FuncionesXML import *

print('MENU')
print('1. Listar todos los pokemons.')
print('2. Mostrar el número de ataques distintos en total.')
print('3. Buscar pokemons por sus tipos.')
print('4. Buscar ataques y quiénes lo pueden aprender.')
print('5. Introducir un pokemon y mostrar sus evoluciones.')
print('0. Salir')
opcion=int(input('Introduzca una opcion:'))

while opcion!=0:

#1
	if opcion==1:
		datos=listar(pokemon)
		for i,j,k in zip(datos[0],datos[1],datos[2]):
			print('nº',j,':',i)
			print(' -Descripción:',k)

#2	
	elif opcion==2:
		movimientos=contar(pokemon)
		ataques=[]
		for i in movimientos:
			if i not in ataques:
				ataques.append(i)
		print(len(ataques))
#3
	elif opcion==3:
		tipo1=input('Introduzca un tipo:')
		tipo2=input('Introduzca un segundo tipo (* para no buscar un segundo tipo):')
		lista=buscar(pokemon,tipo1,tipo2)
		for i in lista:
			print(i)
#4
	elif opcion==4:
		movimiento=input('Introduzca el movimiento a buscar:')
		busqueda=buscar_relacionada(pokemon,movimiento)
		print(movimiento,'pueden aprenderlo:')
		for i in busqueda:
			print('nº',i[1],':',i[0])

#5
	elif opcion==5:
		nombre=input('Introduzca el nombre del pokemon:')
		if libre(pokemon,nombre) == False:
			print('No existe ese Pokemon.')
		else:
			lista_nombres=libre(pokemon,nombre)
			lista_ids=ids_descr(pokemon)
			numeros=[]
			nombres=[]
			descr=[]
			for j in lista_nombres:
				numeros.append(j[1])
				nombres.append(j[0])	
			for i in lista_ids:
				for j in numeros:
					if i[0] == j:
						descr.append(i[1])
			for a,b,c in zip(numeros,nombres,descr):
				print('nº:',a)
				print('  -',b,':',c)

	else:
		print('¡Tiene que ser un valor la lista de opciones!')

	print('MENU')
	print('1. Listar todos los pokemons.')
	print('2. Mostrar el número de ataques distintos en total.')
	print('3. Buscar pokemons por sus tipos.')
	print('4. Buscar ataques y quiénes lo pueden aprender.')
	print('5. Introducir un pokemon y mostrar sus evoluciones.')
	print('0. Salir')
	opcion=int(input('Introduzca una opcion:'))

print('Programa Terminado.')
