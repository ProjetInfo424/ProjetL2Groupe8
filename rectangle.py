def rectangle(posx,posy,longueur,largeur,couleur,taille):
	t=[[0 for x in range(taille)] for x in range (taille)]
	for i in range(posx,longueur+posx,1):
		for j in range(posy,largeur+posy,1):
			t[i][j]=couleur

	print(t)



