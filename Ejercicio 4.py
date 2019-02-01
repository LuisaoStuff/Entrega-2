#	Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

#		Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# 		Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones 
#		de la primera por la segunda en la lista.
#		Eliminar: Me pide una cadena, y la elimina de la lista.

#	El programa te muestra el menú, hasta que introduzcamos la opción 0 de salir.

lista=[]

for i in range(0,int(input("		¿Cuántas palabras vas a introducir?	"))):
	lista.append(str(input("		Dime una palabra:	")).lower())

opcion=1

while opcion!=0:
	print("\n"*30,"		Elige una de las opciones:\n 			1. Contar\n			2. Modificar\n			3. Eliminar\n\n			0. Salir")
	opcion=int(input("\n		Opcion:	"))
	if opcion==1:
		palabra=str(input("			Dame una palabra:	").lower())
		print("\n			La palabra indicada aparece",lista.count(palabra),".\n")
		input("			Pulsa enter para continuar...")
	elif opcion==2:
		palabra=str(input("			Dame una palabra:	").lower())
		palabra2=str(input("			¿Qué palabra quieres sustituir con la primera?	").lower())
		for i in range(0,len(lista)):
			if lista[i].find(palabra)!=-1:
				lista[i]=lista[i].replace(palabra,palabra2)
		input("			Pulsa enter para continuar...")
	elif opcion==3:
		palabra=str(input("			Introduce la palabra a eliminar:	").lower())
		while lista.count(palabra)>0:
			lista.remove(palabra)
		input("			Pulsa enter para continuar...")
	elif opcion==0:
		print("\n"*2)
	else:
		print("			¡Esa opción no existe!\n")
		input("			Pulsa enter para continuar...")