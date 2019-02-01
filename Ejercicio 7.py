#	Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

#		Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# 		Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones 
#		de la primera por la segunda en la lista.
#		Eliminar: Me pide una cadena, y la elimina de la lista.

#	El programa te muestra el menú, hasta que introduzcamos la opción 0 de salir.

lista=[]

for i in range(0,int(input("\n		¿Cuántas nombres vas a introducir?	"))):

	nombre=str(input("\n		Dime el nombre:		").title())
	edad=int(input("		Dime la edad:		"))

	listainfo=[]
	listainfo.append(nombre)
	listainfo.append(edad)

	lista.append(listainfo)


print("		",lista)

opcion=1

while opcion!=0:
	print("\n"*30,"		Elige una de las opciones:\n 			1. Contar\n			2. Modificar\n			3. Eliminar\n\n			0. Salir")
	opcion=int(input("\n		Opcion:	"))
	
	if opcion==1:			#	Contar Nombres
	
		palabra=str(input("			Dame un nombre:	").title())
		contador=0
		for i in range(0,len(lista)):
			if lista[i][0].count(palabra)==1:
				contador=contador+1
		print("\n			",palabra,"aparece",contador,"veces.")
		input("			Pulsa enter para continuar...")	

	elif opcion==2:			#	Modificar Nombres o Edades
		
		palabra=str(input("			Dame un nombre:	").title())
		print("			¿Qué quieres sustituir?\n			(1)Nombres	(2)Edades\n\n				Opcion:",end="	")
		
		stop=False
		while stop==False:
		
			eleccion=int(input())
		
			if eleccion==1:
				palabra2=str(input("			¿Qué nombre quieres sustituir con la primera?	").title())
				edad=int(input("			Concreta la edad original del sujeto:	"))
				for i in range(0,len(lista)):
					if lista[i][0].count(palabra)==1 and lista[i][1]==edad:
						lista[i][0]=lista[i][0].replace(palabra,palabra2)
						print("			",lista,"\n")
						input("			Pulsa enter para continuar...")
						stop=True
						

			elif eleccion==2:
				edad=int(input("			Concreta la edad original del sujeto:	"))
				edad2=int(input("			¿Qué edad quieres introducir?	"))
				for i in range(0,len(lista)):
					if lista[i][0].count(palabra)==1 and lista[i][1]==edad:
						lista[i].remove(lista[i][1])
						lista[i].append(edad2)
						print("			",lista,"\n")
						input("			Pulsa enter para continuar...")
						stop=True
						
			else:
				print("			Elige una opcion válida.\n			(1)Nombres	(2)Edades\n\n				Opcion:",end="	")
			stop=True
	elif opcion==3:
		palabra=str(input("			¿A quién quieres eliminar?	").title())
		edad=int(input("			Concreta la edad del sujeto:	")) 
		for i in range(0,len(lista)):
				if lista[i][0].count(palabra)==1 and lista[i][1]==edad:
					lista.remove(lista[i])
					break
		print("			",lista,"\n")
		input("			Pulsa enter para continuar...")
	
	elif opcion==0:
		print("\n"*2)
	
	else:
		print("			¡Esa opción no existe!\n")
		input("			Pulsa enter para continuar...")