lista=[]

nombre=str(input("\n		¿Cómo se llama?		").title())

while nombre!='*':
	
	edad=int(input("		¿Qué edad tiene?	"))
	
	lista.append(nombre)
	lista.append(edad)

	nombre=str(input("\n		¿Cómo se llama?		").title())
	
sumatorio=0
maximo=lista[1]

for i in range(0,len(lista)):
	if i%2!=0 and lista[i]>maximo:
		maximo=lista[i]
	if i%2!=0:
		sumatorio=sumatorio+lista[i]
print("\n		Alumno(s) con mayor edad:\n\n\n		Nombre:				Edad:\n")

for i in range(0,len(lista)):
	if maximo==lista[i]:
		if len(lista[i-1])>=6:
			print("		",lista[i-1],"			",lista[i])
		else:
			print("		",lista[i-1],"				",lista[i])

media=sumatorio/(len(lista)/2)

print("\n		La media de edades de la clase es:	",media)

nombre=str(input("		Dime un nombre para buscar:	").title())

Encontrado=False
print("\n		Lista de alumno(s) cuyo nombre es",nombre,":\n\n\n		Nombre:				Edad:\n")
for i in range(0,len(lista)):
	if nombre==lista[i]:
		if len(lista[i])>=6:
			print("		",lista[i],"			",lista[i+1])
		else:
			print("		",lista[i],"				",lista[i+1])
		Encontrado=True

if Encontrado:
	print("		",lista.count(nombre),"alumnos cuyo nombre es",nombre,".\n\n		Pulsa enter para continuar...")
	input("		Pulsa enter para continuar...")
else:
	print("		*********************************\n\n		",nombre,"no figura en la lista.\n\n		Pulsa enter para continuar...")
	input("		Pulsa enter para continuar...")

print("\n		Lista de alumnos mayores de edad:\n\n\n		Nombre:				Edad:\n")

for i in range(0,len(lista)):
	if i%2!=0 and lista[i]>=18:
		if len(lista[i-1])>=6:
			print("		",lista[i-1],"			",lista[i])
		else:
			print("		",lista[i-1],"				",lista[i])

print("\n")