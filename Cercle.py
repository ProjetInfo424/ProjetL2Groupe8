
from math import sqrt
#On a besoin de la bibliotheque python math pour utiliser la fonction racine carrée
def cercle(x, y, rayon, hauteur_image,largeur_image, couleurf, couleuri ):
#Fonction qui dessine un cercle dans une image. Elle a pour arguments :
#x : abscisse du centre du cercle
#y : ordonnée du centre du cercle        
#rayon : rayon du cercle
#couleurf : couleur des pixels qui forment le cercle
#couleuri: couleur des pixels qui forment l'image
#hauteur_image : la hauteur de l'image
#largeur_image : la largeur de l'image        

	t=[[couleuri for x in range(largeur_image)] for x in range(hauteur_image)]

	for i in range (hauteur_image):
		for j in  range (largeur_image):
			if sqrt((x-i)**2 + (y-j)**2)<=rayon:
                        #Pour chaque pixel on verifie si il est a une distance inferieure ou egale au rayon du centre.
				t[i][j]=couleurf;
	for i in range(hauteur_image):
		print("");
	
		for j in range(largeur_image):
			print(str(t[i][j]),end=" ");
def save():

def sauve(image,fichier):
    """Sauvegarde l'image dans un fichier.
        L'extension du fichier est automatiquement ajoutÃ©e."""
           
           f = open(fichier , "w")
               f.write("P2" + "\n"+image)

sauve(cercle(10, 10, 7, 1, 30,30),cercle.pgm)

