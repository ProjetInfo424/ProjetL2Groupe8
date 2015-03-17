def Bresenham(x1, y1, x2, y2, posx):
#fonction qui donne l'ordonnée d'un point en fonction de son abscisse
#pour qu'il soit aligné le plus possible avec la droite qui relie deux autres points.
#Cette fonction s'inspire de l'algorithme de Bresenham et a pour arguments :
#x1 : abscisse du premier point
#y1 : ordonnée du premier point    
#
#
#
    return((y2-y1)//(x2-x1)*(posx-x1)+y1+1//2)

def Triangle(x1, y1, x2, y2, x3, y3, couleur, hauteur_image, largeur_image):
    t=[[0 for x in range(largeur_image)] for x in range(hauteur_image)]


    if y1==y2:
        for i in range(hauteur_image):
            for j in range (largeur_image):
                if j>=x1 and j<=x2 and i==y1:
                    t[i][j]=couleur;
    for i in range(hauteur_image):
        print("");
        for j in range(largeur_image):
            print(str(t[i][j]),end=" ");                        
                            




##Triangle(2,6,6,6,5,3,1,10,10)
                        
                
            elif y1=y3:
                for i in range(hauteur_image):
                    for j in range (largeur_image):
##                        
##            elif y2=y3:
##                for i in range(hauteur_image):
##                    for j in range (largeur_image):
                
                    
