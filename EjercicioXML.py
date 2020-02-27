from lxml import etree
pokemon = etree.parse('pokemon.xml')
from FuncionesXML import *

#datos=listar(pokemon)
#for i,j,k in zip(datos[0],datos[1],datos[2]):
#	print('nº',j,':',i)
#	print(' -Descripción:',k)

#movimientos=contar(pokemon)
#ataques=[]
#for i in movimientos:
#	if i not in ataques:
#		ataques.append(i)
#print(len(ataques))

#tipo1=input('Introduzca un tipo:')
#tipo2=input('Introduzca un segundo tipo (* para no buscar un segundo tipo):')
#lista=buscar(pokemon,tipo1,tipo2)
#for i in lista:
#	print(i)

#movimiento=input('Introduzca el movimiento a buscar:')
#busqueda=buscar_relacionada(pokemon,movimiento)
#print(movimiento,'pueden aprenderlo:')
#for i in busqueda:
#	print('nº',i[1],':',i[0])

nombre=input('Introduzca el nombre del pokemon:')
lista2=libre(pokemon,nombre)
print(lista2)