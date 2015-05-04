from math import sqrt
from sys import argv
#On a besoin de la bibliotheque python math pour utiliser la fonction racine carrée

def couleur_ppm (couleur) :
    if couleur == "blanc" :
        return [255,255,255]
    if couleur == "noir" :
        return [0,0,0]
    if couleur == "bleu" :
        return [0,0,255]
    if couleur == "jaune" :
        return [255,255,0]
    if couleur == "rouge" :
        return [255,0,0]
    if couleur == " violet":
        return [102, 0, 153]
    if couleur == "vert" :
        return [0 ,255, 0]
    if couleur == "rose" :
        return [253, 108, 158]
    if couleur == "orange":
        return [237, 127, 16]

def matrice(largeuri,hauteuri,couleuri):
    couleur_im = couleur_ppm(couleuri);
    tmat=[[couleur_im for x in range(hauteuri)] for x in range (largeuri)];
    return tmat



    
def rectangle(posx,posy,largeurf,hauteurf,couleurf,largeuri,hauteuri,couleuri):

    ## Cette procedure permet de créer un rectangle. Ses paramètres sont:
    ## posx --> position de la figure par rapport a l'abscisse 
    ## posy --> position de la figure par rapport a l'ordonnée
    ## largeurf --> largeur de la figure (horizontale) 
    ## hauteurf --> hauteur de la figure (verticale)
    ## largeuri --> largeur de l'image (horizontale)
    ## hauteuri --> hauteur de l'image (verticale)
    ## couleurf --> couleur de la figure (un entier)
    ## couleuri --> couleur de l'image (un entier)

    couleur_fi = couleur_ppm(couleurf)


    print("P3"+ "\n" + str(largeuri) + " " + str(hauteuri) +"\n" + "255");

    t=matrice(largeuri,hauteuri,couleuri);
    tailleh=largeurf+posx;
    taillev=hauteurf+posy;
    
    if tailleh > largeuri or taillev > hauteuri:
        print("Votre dessin a depassé la matrice");
    else:
        
        for i in range(posy,taillev,1):
            for j in range(posx,tailleh,1): 
                t[j][i]=couleur_fi;
    for k in range(hauteuri):
        
        for l in range(largeuri):
            enleve = str(t[l][k])
            enleve = enleve.replace("[", "")
            enleve = enleve.replace("]", "")
            enleve = enleve.replace(",", "")
            print(enleve,end= " ");
        print("");

       



def cercle(x, y, rayon, hauteuri,largeuri,couleuri ,couleurf) :
#Fonction qui dessine un cercle dans une image. Elle a pour arguments :
#x : abscisse du centre du cercle
#y : ordonnée du centre du cercle        
#rayon : rayon du cercle
#couleurf : couleur des pixels qui forment le cercle
#couleuri: couleur des pixels qui forment l'image
#hauteuri : la hauteur de l'image
#largeuri : la largeur de l'image
    print("P3"+ "\n" + str(largeuri) + " "+ str(hauteuri)+"\n" + "255");

    t= matrice(largeuri,hauteuri,couleuri);
    couleur_fi = couleur_ppm(couleurf)
    
    for i in range (hauteuri):
        for j in  range (largeuri):
            if sqrt((x-j)**2 + (y-i)**2)<=rayon:
            #Pour chaque pixel on verifie si il est a une distance inferieure ou egale au rayon du centre.
                t[j][i]=couleur_fi;
    for k in range(hauteuri):
        
        for l in range(largeuri):
            enleve = str(t[l][k])
            enleve = enleve.replace("[", "")
            enleve = enleve.replace("]", "")
            enleve = enleve.replace(",", "")
            print(enleve,end= " ");
        print("");


def trace_segment(t,x0,y0,x1,y1,couleurf):
    
    couleur_fi = couleur_ppm(couleurf);
    tmp=0
    tmp2=0
    if x1 < x0 :
        tmp=x0
        x0=x1
        x1=tmp
        tmp2=y0
        y0=y1
        y1=tmp2 
        
    deltax = x1-x0
    deltay = y1-y0
    error = 0
    deltaerror = abs(deltay/deltax)
    y=y0
    sign=1
    if y1-y0< 0:
        sign= -1
    for x in range(x0,x1,1):
        t[x][y]=couleur_fi
        error=error+deltaerror
        while error >= 0.5:
            t[x][y]= couleur_fi
            y=y+sign
            error=error-1
            
    
def triangle_rempli(t,x0,y0,x1,y1,x2,y2,largeuri,hauteuri,couleurf):
    compteur=0
    liste =[]
    couleur_fi = couleur_ppm(couleurf)
    
    for i in range (hauteuri):
        for j in range (largeuri):
            if t[i][j] == couleur_fi:
                liste = liste + [j]
                compteur = compteur + 1
        if compteur > 1:
            for x in range(liste[0],liste[len(liste)-1],1):
                t[i][x]= couleur_fi
            compteur =0  
    
    

def triangle(x0,y0,x1,y1,x2,y2,largeuri,hauteuri, couleuri ,couleurf):

    print("P3"+ "\n" + str(largeuri) + " "+ str(hauteuri)+"\n" + "255");  

    t=matrice(largeuri,hauteuri,couleuri);
    
    trace_segment(t,x0,y0,x1,y1,couleurf);
    trace_segment(t,x1,y1,x2,y2,couleurf);
    trace_segment(t,x2,y2,x0,y0,couleurf);
    triangle_rempli(t,x0,y0,x1,y1,x2,y2,largeuri,hauteuri,couleurf);
    

    for k in range(hauteuri):
        
        for l in range(largeuri):
            enleve = str(t[l][k])
            enleve = enleve.replace("[", "")
            enleve = enleve.replace("]", "")
            enleve = enleve.replace(",", "")
            print(enleve,end= " ");
        print("");

def menu(forme):

          
    if forme == "rectangle" :
        
        posx= int(argv[2])
        posy = int(argv[3])
        largeurf =  int(argv[4])
        hauteurf = int( argv[5] )
        couleurf =str( argv[6] )
        largeuri=int(argv[7])
        hauteuri=  int( argv[8] )
        couleuri=str(argv[9])
        rectangle(posx,posy,largeurf,hauteurf,couleurf,largeuri,hauteuri,couleuri);
       
    if forme == "cercle" :

        x = int(argv[2])
        y = int(argv[3])
        rayon =  int(argv[4])
        hauteuri = int( argv[5] )
        largeuri =int( argv[6] )
        couleuri=str(argv[7])
        couleurf=  str( argv[8] )
        
        cercle(x, y, rayon, hauteuri,largeuri,couleuri ,couleurf)        
        
  
        
    if forme == "triangle" :
        
        x0= int(argv[2])
        y0 = int(argv[3])
        x1 =  int(argv[4])
        y1 = int( argv[5] )
        x2 =int( argv[6] )
        y2=int(argv[7])
        largeuri=  int( argv[8] )
        hauteuri=int(argv[9])
        couleuri=str(argv[10])
        couleurf=str(argv[11])

        
        triangle(x0,y0,x1,y1,x2,y2,largeuri,hauteuri, couleuri ,couleurf)

if __name__ == '__main__' :

   menu(argv[1]);
    

  
    
            
            
            
                

                

  

