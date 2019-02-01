#	Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes 
#	listas (en las que no debe haber repeticiones):

#    Lista de palabras que aparecen en las dos listas.
#    Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#    Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#    Lista de palabras que aparecen en ambas listas.

listaA=[]
limite=int(input("\n		Dime cuántas palabras tiene la primera lista:	"))

for i in range(0,limite):
	listaA.append(str(input("		Dime una palabra:	")).title())
	#listaA[i]=listaA[i].upper()
listaAR=[]
for i in range(0,limite):
	if listaA.count(listaA[i])==2:
		listaAR.append(listaA[i])
for i in range(0,len(listaAR)):
	if listaA.count(listaAR[i])>1:
		listaA.remove(listaAR[i])
print("\n		La primera lista es:\n		",listaA)

listaB=[]
limite2=int(input("\n		Dime cuántas palabras tiene la segunda lista:	"))

for i in range(0,limite2):
	listaB.append(str(input("		Dime una palabra:	")).title())
	#listaB[i]=listaB[i].upper()

listaBR=[]
for i in range(0,limite2):
	if listaB.count(listaB[i])>=2:
		listaBR.append(listaB[i])
for i in range(0,len(listaBR)):
	if listaB.count(listaBR[i])>1:
		listaB.remove(listaBR[i])

print("\n		La segunda lista es:\n		",listaB)


listaCoinc=[]
listaBS=[]
listaAS=[]
listaT=[]

for i in range(0,len(listaB)):
	if listaB[i] in listaA:
		listaCoinc.append(listaB[i])
	else:
		listaBS.append(listaB[i])
	listaT.append(listaB[i])
for i in range(0,len(listaA)):
	if listaA[i] not in listaB:
		listaAS.append(listaA[i])
		listaT.append(listaA[i])

print("\n		Palabras que aparecen en las dos listas:	",listaCoinc)
print("\n		Palabras que sólo aparecen en la primera lista:	",listaAS)
print("\n		Palabras que sólo aparecen en la segunda lista:	",listaBS)
print("\n		Todas las palabras:\n		",listaT,"\n\n")
