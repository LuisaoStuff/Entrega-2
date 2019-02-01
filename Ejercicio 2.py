#	Escribe una programa que pida una cadena de caracteres y diga si no tiene caracteres repetidos.

cad=str(input("\n		Dame una cadena:	"))

SeRepite=False

for i in range(0,len(cad)):

	if (cad.upper()).count(cad[i].upper())>1:
		SeRepite=True

if SeRepite==False:
	print("\n		La cadena no tiene caracteres repetidos.\n")
else:
	print("\n		La cadena tiene caracteres repetidos.\n")

