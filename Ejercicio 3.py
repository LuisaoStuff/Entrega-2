#	Tenemos la siguiente variable definida en nuestro programa:
#	En esa cadena se definen nombres de poblaciones y las temperaturas máximas y mínimas 
#	de dichas poblaciones durante un día.
#	Realiza un programa que muestre el nombre de las poblaciones y la temperatura media.
#	demás el programa te debe pedir el nombre de una población y nos debe dar la temperatura 
#	máxima y mínima (si la población no existe se debe dar une error.)

temperaturas='''
	Utrera,29,12
	Dos Hermanas,32,14
	Sevilla,30,15
	Alcalá de Guadaíra,31,14
'''

lista = temperaturas.split("\n\t")	# \
temperatura=','.join(lista)			#  |---- Esto es para "limpiar" la lista de los saltos de linea y las tabulaciones
lista=temperatura.split(",")		# /

print("\n")

for i in range(0,len(lista)):
	if lista[i].find("a")!=-1:		#	Cada vez que encuentre la letra "a" (letra común a todas las ciudades), lo muesta por pantalla y hace la media con los dos números siguientes
		print("		 ",lista[i],": Su temperatura media es:",(int(lista[i+1])+int(lista[i+2]))/2)

Validar=False

while Validar==False:

	#Ciudad=str(input("\n		  Dime el nombre de la ciudad:	"))
	Ciudad=(str(input("\n		  Dime el nombre de la ciudad:	"))).title()
	if lista.count(Ciudad)==1:

		for i in range(0,len(lista)):
			if Ciudad==lista[i]:
				print("		 ",lista[i],":\n\n			-Temperatura máxima:",lista[i+1],"\n			-Temperatura mínima:",lista[i+2],"\n")
		Validar=True
	else:
		print("		Esa ciudad no está en la lista! Prueba de nuevo.\n")