from math import sqrt
#On a besoin de la bibliotheque python math pour utiliser la fonction racine carrée
def cercle(x, y, rayon, couleur, hauteur_image,largeur_image ):
#Fonction qui dessine un cercle dans une image. Elle a pour arguments :
#x : abscisse du centre du cercle
#y : ordonnée du centre du cercle        
#rayon : rayon du cercle
#couleur : couleur des pixels qui forment le cercle
#hauteur_image : la hauteur de l'image
#largeur_image : la largeur de l'image        

	t=[[0 for x in range(largeur_image)] for x in range(hauteur_image)]

	for i in range (hauteur_image):
		for j in  range (largeur_image):
			if sqrt((x-i)**2 + (y-j)**2)<=rayon:
                        #Pour chaque pixel on verifie si il est a une distance inferieure ou egale au rayon
				t[i][j]=couleur;
	for i in range(hauteur_image):
		print("");
	
		for j in range(largeur_image):
			print(str(t[i][j]),end=" ");
