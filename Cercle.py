from math import sqrt
def cercle(x, y, rayon, couleur, taille):
	t=[[0 for x in range(taille)] for x in range(taille)]
	for i in range (x, taille, 1):
		for j in  range (y, taille, 1):
			if sqrt((x-i)**2 + (y-j)**2)<=rayon:
				t[i][j]=couleur
