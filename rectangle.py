def rectangle(posx,posy,longueur,largeur,couleur,couleur2,taille):
    t=[[couleur2 for x in range(taille)] for x in range (taille)]
    taillev=longueur+posx;
    tailleh=largeur+posy;
    if taillev > taille or tailleh > taille:
        print("Votre dessin a depassé la matrice");
    else:
        
        for i in range(posx,longueur+posx,1):
            for j in range(posy,largeur+posy,1):
                t[i][j]=couleur;
        for i in range(taille):
            print("");
    
            for j in range(taille):
                print(str(t[i][j]),end=" ");

    



