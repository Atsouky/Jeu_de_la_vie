"""
Programme jeu de la vie rÃ©alisÃ© par nom, prÃ©nom, classe
"""
import pygame
from random import *
#region------------------------------------------------------------__Init__-----------------------------------------------------------------------------------------
#variables de l'Ã©cran
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 32
CELLWIDTH = WINDOWWIDTH // CELLSIZE
CELLHEIGHT = WINDOWHEIGHT // CELLSIZE

FPS=1   #vitesse du jeu

ROUGE=(255,0,0)
NOIR=(0,0,0)
BLANC=(255,255,255)
VERT=(0,255,0)

clock = pygame.time.Clock()
pygame.init()
fenetre = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Jeu de la vie")
font = pygame.font.Font('freesansbold.ttf', 20)
#endregion





#Trace la grille
def tracerGrille():
    for i in range(0,WINDOWWIDTH+1,CELLSIZE):
        pygame.draw.line(fenetre,ROUGE,(0+i,0),(0+i,480),1)
    for j in range(0,WINDOWHEIGHT+1,CELLSIZE):
        pygame.draw.line(fenetre,ROUGE,(0,0+j),(640,0+j),1)
    pass


#initialise un dictionnaire de cellules CELLWIDTH*CELLHEIGHT {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0, ....(17, 14): 0, (18, 14): 0, (19, 14): 0}
#les cellules seront toutes mortes
def initialiserCellules():
    vie = {(0,0):0,(1,0):0,(2,0):0,(3,0):0,(4,0):0,(5,0):0,(6,0):0,(7,0):0,(8,0):0,(9,0):0,(10,0):0,(11,0):0,(12,0):0,(13,0):0,(14,0):0,(15,0):0,(16,0):0,(17,0):0,(18,0):0,(19,0):0,
           (0,1):0,(1,1):0,(2,1):0,(3,1):0,(4,1):0,(5,1):0,(6,1):0,(7,1):0,(8,1):0,(9,1):0,(10,1):0,(11,1):0,(12,1):0,(13,1):0,(14,1):0,(15,1):0,(16,1):0,(17,1):0,(18,1):0,(19,1):0,
           (0,2):0,(1,2):0,(2,2):0,(3,2):0,(4,2):0,(5,2):0,(6,2):0,(7,2):0,(8,2):0,(9,2):0,(10,2):0,(11,2):0,(12,2):0,(13,2):0,(14,2):0,(15,2):0,(16,2):0,(17,2):0,(18,2):0,(19,2):0,
           (0,3):0,(1,3):0,(2,3):0,(3,3):0,(4,3):0,(5,3):0,(6,3):0,(7,3):0,(8,3):0,(9,3):0,(10,3):0,(11,3):0,(12,3):0,(13,3):0,(14,3):0,(15,3):0,(16,3):0,(17,3):0,(18,3):0,(19,3):0,
           (0,4):0,(1,4):0,(2,4):0,(3,4):0,(4,4):0,(5,4):0,(6,4):0,(7,4):0,(8,4):0,(9,4):0,(10,4):0,(11,4):0,(12,4):0,(13,4):0,(14,4):0,(15,4):0,(16,4):0,(17,4):0,(18,4):0,(19,4):0,
           (0,5):0,(1,5):0,(2,5):0,(3,5):0,(4,5):0,(5,5):0,(6,5):0,(7,5):0,(8,5):0,(9,5):0,(10,5):0,(11,5):0,(12,5):0,(13,5):0,(14,5):0,(15,5):0,(16,5):0,(17,5):0,(18,5):0,(19,5):0,
           (0,6):0,(1,6):0,(2,6):0,(3,6):0,(4,6):0,(5,6):0,(6,6):0,(7,6):0,(8,6):0,(9,6):0,(10,6):0,(11,6):0,(12,6):0,(13,6):0,(14,6):0,(15,6):0,(16,6):0,(17,6):0,(18,6):0,(19,6):0,
           (0,7):0,(1,7):0,(2,7):0,(3,7):0,(4,7):0,(5,7):0,(6,7):0,(7,7):0,(8,7):0,(9,7):0,(10,7):0,(11,7):0,(12,7):0,(13,7):0,(14,7):0,(15,7):0,(16,7):0,(17,7):0,(18,7):0,(19,7):0,
           (0,8):0,(1,8):0,(2,8):0,(3,8):0,(4,8):0,(5,8):0,(6,8):0,(7,8):0,(8,8):0,(9,8):0,(10,8):0,(11,8):0,(12,8):0,(13,8):0,(14,8):0,(15,8):0,(16,8):0,(17,8):0,(18,8):0,(19,8):0,
           (0,9):0,(1,9):0,(2,9):0,(3,9):0,(4,9):0,(5,9):0,(6,9):0,(7,9):0,(8,9):0,(9,9):0,(10,9):0,(11,9):0,(12,9):0,(13,9):0,(14,9):0,(15,9):0,(16,9):0,(17,9):0,(18,9):0,(19,9):0,
           (0,10):0,(1,10):0,(2,10):0,(3,10):0,(4,10):0,(5,10):0,(6,10):0,(7,10):0,(8,10):0,(9,10):0,(10,10):0,(11,10):0,(12,10):0,(13,10):0,(14,10):0,(15,10):0,(16,10):0,(17,10):0,(18,10):0,(19,10):0,
           (0,11):0,(1,11):0,(2,11):0,(3,11):0,(4,11):0,(5,11):0,(6,11):0,(7,11):0,(8,11):0,(9,11):0,(10,11):0,(11,11):0,(12,11):0,(13,11):0,(14,11):0,(15,11):0,(16,11):0,(17,11):0,(18,11):0,(19,11):0,
           (0,12):0,(1,12):0,(2,12):0,(3,12):0,(4,12):0,(5,12):0,(6,12):0,(7,12):0,(8,12):0,(9,12):0,(10,12):0,(11,12):0,(12,12):0,(13,12):0,(14,12):0,(15,12):0,(16,12):0,(17,12):0,(18,12):0,(19,12):0,
           (0,13):0,(1,13):0,(2,13):0,(3,13):0,(4,13):0,(5,13):0,(6,13):0,(7,13):0,(8,13):0,(9,13):0,(10,13):0,(11,13):0,(12,13):0,(13,13):0,(14,13):0,(15,13):0,(16,13):0,(17,13):0,(18,13):0,(19,13):0,
           (0,14):0,(1,14):0,(2,14):0,(3,14):0,(4,14):0,(5,14):0,(6,14):0,(7,14):0,(8,14):0,(9,14):0,(10,14):0,(11,14):0,(12,14):0,(13,14):0,(14,14):0,(15,14):0,(16,14):0,(17,14):0,(18,14):0,(19,14):0}
           
   
    return vie



#active alÃ©atoirement les cellules (mise Ã  1) {(0, 0): 0, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1, etc...
def generationAleatoire(vie):
    for i in range(0,20):
        for j in range(0,14):
            vie[(i,j)]=randint(0,1)
    return vie


#remplir la fenetre avec un rectangle vert si la cellule est vivante, noir sinon morte)
def remplirGrille(vie):
    for item in vie:
        x = item[0]
        y = item[1]
        y = y * CELLSIZE
        x = x * CELLSIZE
        if vie[item] == 0:
            pygame.draw.rect(fenetre, NOIR, (x, y, CELLSIZE, CELLSIZE))
        if vie[item] == 1:
            pygame.draw.rect(fenetre, VERT, (x, y, CELLSIZE, CELLSIZE))

#DÃ©termine combien de voisins sont en vie
#rappel item est un tuple (x,y) contenant la position de la cellule.
def voisins(item,vie):
    nbVoisins = 0
    for x in range (-1,2):
        for y in range (-1,2):
            #A complÃ©ter
            pass
    return nbVoisins

#calcule la prochaine Ã©tape, retourne un nouveau dictionnaire
def prochaineEtape(vie):
    nouvelleVie= {}
    for item in vie:
        #recupÃ¨re le nombre de voisins d'une cellule
        #A complÃ©ter
        pass

    return nouvelleVie



vie=initialiserCellules()
vie=generationAleatoire(vie)

#region------------------------------------------------------------__Loop__-----------------------------------------------------------------------------------------
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                vie=prochaineEtape(vie)     #manuel

    fenetre.fill(NOIR)
    remplirGrille(vie)
    tracerGrille()
    pygame.display.update() #mets Ã  jour la fentre graphique
    vie=prochaineEtape(vie)  #pour une animation
    clock.tick(FPS)

pygame.quit()

#endregion