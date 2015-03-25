def rectangle(posx,posy,largeurf,hauteurf,largeuri,hauteuri,couleurf,couleuri):

    ## Cette procedure permet de créer un rectangle. Ses paramètres sont:
    ## posx --> position de la figure par rapport a l'abscisse 
    ## posy --> position de la figure par rapport a l'ordonnée
    ## largeurf --> largeur de la figure (horizontale) 
    ## hauteurf --> hauteur de la figure (verticale)
    ## largeuri --> largeur de l'image (horizontale)
    ## hauteuri --> hauteur de l'image (verticale)
    ## couleurf --> couleur de la figure (un entier)
    ## couleuri --> couleur de l'image (un entier)
    
    t=[[couleuri for x in range(largeuri)] for x in range (hauteuri)]
    
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

    



