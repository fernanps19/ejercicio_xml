from lxml import etree
pokemon = etree.parse('pokemon.xml')
from FuncionesXML import *

#datos=listar(pokemon)
#for i,j,k in zip(datos[0],datos[1],datos[2]):
#	print('nº',j,':',i)
#	print(' -Descripción:',k)

movimientos=contar(pokemon)
ataques=[]
for i in movimientos:
	if i not in ataques:
		ataques.append(i)
print(len(ataques))