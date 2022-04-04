i = 0
j = 0
nombreColone = int(input("Nombre de colones ?\n"))
nombreLigne = int(input("Nombre de ligne ?.\n"))

while  j < nombreLigne:
	
	while  i < nombreColone :
		
		print("@" , end = '')
		
		i = i + 1 

	print("")	
	
	i = 0

	j = j + 1
