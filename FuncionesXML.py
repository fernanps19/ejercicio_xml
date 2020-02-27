#1. Listar Información: mostrar el nombre de cada pokemon con su id y su descripción.
def listar(pokemon):
	nombres=pokemon.xpath('//pokemon/name/text()')
	ids=pokemon.xpath('//pokemon/@id')
	descripciones=pokemon.xpath('//pokemon/description/text()')
	return nombres,ids,descripciones

#2. Contar: Mostrar el número de ataques distintos en total.
def contar(pokemon):
	ataques=pokemon.xpath('//pokemon/moves/move/name/text()')
	return ataques

#3. Buscar: Introducir por teclado uno o dos tipos y mostrar 
#todos los pokemon que poseen esos tipos.
def buscar(pokemon,tipo1,tipo2):
	nombre=[]
	lista=pokemon.xpath('/pokedex/pokemon')
	for i in lista:
		if tipo2 == '*':
			if tipo1 in i.xpath('./type/text()'):
				nombre.append(i.xpath('./name/text()')[0])
		elif tipo1 in i.xpath('./type/text()') and tipo2 in i.xpath('./type/text()'):
			nombre.append(i.xpath('./name/text()')[0])
	return nombre


#4. Buscar informacion relacionada: Introducir por teclado un movimiento y
#mostrar los pokemon con su id que pueden aprender ese movimiento.
def buscar_relacionada(pokemon,movimiento):
	nombre=[]
	ids=[]
	lista=pokemon.xpath('/pokedex/pokemon')
	for i in lista:
		if movimiento in i.xpath('./moves/move/name/text()'):
			nombre.append(i.xpath('./name/text()')[0])
			ids.append(i.xpath('./@id')[0])
	return zip(nombre,ids)

#5. Libre: Introducir por teclado el nombre de un pokemon y 
#mostrar el nombre de sus evoluciones, si tiene, con la id de cada uno y su descripción.
def libre(pokemon,nombre):
	lista=pokemon.xpath('/pokedex/pokemon')
	for i in lista:
		if nombre==i.xpath('./name/text()'):
			 return i.xpath('./evolutions/evolution/name/text()')