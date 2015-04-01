from math import sqrt
#On a besoin de la bibliotheque python math pour utiliser la fonction racine carrée

def matrice(largeuri,hauteuri,couleuri):
    t=[[couleuri for x in range(largeuri)] for x in range (hauteuri)];
    
    return t
    
def rectangle(t,posx,posy,largeurf,hauteurf,couleurf,couleuri):

    ## Cette procedure permet de créer un rectangle. Ses paramètres sont:
    ## posx --> position de la figure par rapport a l'abscisse 
    ## posy --> position de la figure par rapport a l'ordonnée
    ## largeurf --> largeur de la figure (horizontale) 
    ## hauteurf --> hauteur de la figure (verticale)
    ## largeuri --> largeur de l'image (horizontale)
    ## hauteuri --> hauteur de l'image (verticale)
    ## couleurf --> couleur de la figure (un entier)
    ## couleuri --> couleur de l'image (un entier)
    
    
   
    tailleh=largeurf+posx;
    taillev=hauteurf+posy;
    
    if tailleh > largeuri or taillev > hauteuri:
        print("Votre dessin a depassé la matrice");
    else:
        
        for i in range(posy,hauteurf+posy,1):
            for j in range(posx,largeurf+posx,1):
                t[i][j]=couleurf;
    for i in range(hauteuri):
        print("");
        for j in range(largeuri):
            print(str(t[i][j]),end= " ");
       



##def cercle(x, y, rayon, hauteuri,largeuri, couleurf, couleuri ):
###Fonction qui dessine un cercle dans une image. Elle a pour arguments :
###x : abscisse du centre du cercle
###y : ordonnée du centre du cercle        
###rayon : rayon du cercle
###couleurf : couleur des pixels qui forment le cercle
###couleuri: couleur des pixels qui forment l'image
###hauteuri : la hauteur de l'image
###largeuri : la largeur de l'image        
##
##    t= matrice(largeuri,hauteuri,couleuri);
##
##    for i in range (hauteuri):
##        for j in  range (largeuri):
##            if sqrt((x-i)**2 + (y-j)**2)<=rayon:
##            #Pour chaque pixel on verifie si il est a une distance inferieure ou egale au rayon du centre.
##                t[i][j]=couleurf;
##
##
##def trace_segment(t,x0,y0,x1,y1,couleurf):
##
##    tmp=0
##    tmp2=0
##    if x1 < x0 :
##        tmp=x0
##        x0=x1
##        x1=tmp
##        tmp2=y0
##        y0=y1
##        y1=tmp2 
##        
##    deltax = x1-x0
##    deltay = y1-y0
##    error = 0
##    deltaerror = abs(deltay/deltax)
##    y=y0
##    sign=1
##    if y1-y0< 0:
##        sign= -1
##    for x in range(x0,x1,1):
##        t[x][y]=couleurf
##        error=error+deltaerror
##        while error >= 0.5:
##            t[x][y]= couleurf
##            y=y+sign
##            error=error-1
##            
##    
##
##    
##    
##
##def triangle(x0,y0,x1,y1,x2,y2,largeuri,hauteuri,couleurf,couleuri):
##    
##
##    t= matrice(largeuri,hauteuri,couleuri);
##
##    print( "P0 = ({},{})".format( x0, y0 ) )
##    print( "P1 = ({},{})".format( x1, y1 ) )
##    print( "P2 = ({},{})".format( x2, y2 ) )
##    
##    trace_segment(t,x0,y0,x1,y1,couleurf);
##    trace_segment(t,x1,y1,x2,y2,couleurf);
##    trace_segment(t,x2,y2,x0,y0,couleurf);
##
if __name__ == '__main__':
    t= matrice(largeuri,hauteuri,couleuri)
    
