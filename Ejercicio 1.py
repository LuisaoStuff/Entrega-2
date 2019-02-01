#	Realiza un programa que pida un cadena. A continuación debe pedir otra cadena. El programa debe 
#	buscar la segunda cadena en la primera (ignorando mayúsculas o minúsculas) y podrá responder una
#	de las siguientes opciones:

#    	La segunda cadena es una subcadena de la primera
#   	La segunda cadena no es una subcadena de la primera

cad1=str(input("\n		Cadena 1:	"))
cad2=str(input("\n		Cadena 2:	"))

if cad2.upper() in cad1.upper():
	print("\n		",cad2,"está en",cad1,".\n")
else:
	print("\n		",cad2,"no está en",cad1,".\n")
