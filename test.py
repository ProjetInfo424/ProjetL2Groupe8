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




def triangle (larg,longe, couleur):
    ma=[couleur]
    for i in range (0,longe,1):
        for j in range(0,longe,1):
            if i==j:
                ma[i][j]=[couleur][couleur]
            if j==0:
                ma[i][j]=[couleur][couleur]
        if i==longe:
            ma[i][j]=[couleur][couleur]
            else:
                ma[i][j]=[0][0]
        print (ma[i][j])







