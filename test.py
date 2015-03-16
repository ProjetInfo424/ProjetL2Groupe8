##!/usr/bin/env python
#
#
##Variables globales
#
#from Tkinter import *
#import sys
#import signal
#
#
#
#largeur = 0
#longueur = 0
#format = None
#image = None
#
#noir = 0
#blanc= 255
#
#
#################################################################
#"enregistrer l'image dans un fichier "
#################################################################
#def save(image, fichier):
#    f = open ("fichier" , "w")
#    f.write(image)
#
#
#
#################################################################
#"Image vide  "
#################################################################
#def fenetre():
#    global _fen
#    global _image
#
#    _fen = Tk()
#    _fen.title("PGM")
#    _image = Canvas(_fen , width = 500 , height = 500)
#    _image.pack()
#    _fen.mainloop()
#
#fenetre()
#



def triangle (taille, couleur):
    tab=[[]]
    for i in range (taille):
        for j in range(taille):
            
   
            if i==j:
                print(tab[couleur][couleur])
            if j==0:
                tab[i][j]=tab[couleur][couleur]
            if i== taille:
                ttab[i][j]=tab[couleur][couleur]
            else:
                tab[i][j]=tab[0][0]
    print(tab)

triangle(5,5)







