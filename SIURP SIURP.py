import pygame

# Initialisation de Pygame
pygame.mixer.init()
pygame.init()

# Dimentions de la fenetre principale
largeur_image = 1600
hauteur_image = 800

# Définition de la taille de la fenêtre
largeur_fenetre = largeur_image
hauteur_fenetre = hauteur_image

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Chargement des images jouant des sons ( les miniatures )
image1 = pygame.image.load("super.png")
image2 = pygame.image.load("l'eau.png")
image3 = pygame.image.load("jeanne.png")
image4 = pygame.image.load("internet.png")
image5 = pygame.image.load("duriff.png")
image6 = pygame.image.load("bizarre.png")
image7 = pygame.image.load("ben voyons.png")
image8 = pygame.image.load("oui oui.png")
image9 = pygame.image.load("decide.png")
image10 = pygame.image.load("broke.png")
image11 = pygame.image.load("veronique.png")
image12 = pygame.image.load("respect.png")
image13 = pygame.image.load("binaire.png")
image14 = pygame.image.load("mer noire.png")
image15 = pygame.image.load("drame.png")
image16 = pygame.image.load("sensibilite.png")


# Chargement des sons
son1 = pygame.mixer.Sound("super.wav")
son2 = pygame.mixer.Sound("l'eau.wav")
son3 = pygame.mixer.Sound("jeanne.wav")
son4 = pygame.mixer.Sound("internet.wav")
son5 = pygame.mixer.Sound("duriff.wav")
son6 = pygame.mixer.Sound("bizarre.wav")
son7 = pygame.mixer.Sound("ben voyons.wav")
son8 = pygame.mixer.Sound("oui oui.wav")
son9 = pygame.mixer.Sound("decide.wav")
son10 = pygame.mixer.Sound("broke.wav")
son11 = pygame.mixer.Sound("veronique.wav")
son12 = pygame.mixer.Sound("respect.wav")
son13 = pygame.mixer.Sound("binaire.wav")
son14 = pygame.mixer.Sound("mer noire.wav")
son15 = pygame.mixer.Sound("drame.wav")
son16 = pygame.mixer.Sound("sensibilite.wav")



# Positionnement des miniatures
image1_rect = image1.get_rect()
image1_rect.topleft = (0, 0)

image2_rect = image2.get_rect()
image2_rect.topleft = (400, 0)

image3_rect = image3.get_rect()
image3_rect.topleft = (800, 0)

image4_rect = image4.get_rect()
image4_rect.topleft = (1200, 0)

image5_rect = image5.get_rect()
image5_rect.topleft = (0, 200)

image6_rect = image6.get_rect()
image6_rect.topleft = (400, 200)

image7_rect = image7.get_rect()
image7_rect.topleft = (800, 200)

image8_rect = image8.get_rect()
image8_rect.topleft = (1200, 200)

image9_rect = image9.get_rect()
image9_rect.topleft = (0, 400)

image10_rect = image10.get_rect()
image10_rect.topleft = (400, 400)

image11_rect = image11.get_rect()
image11_rect.topleft = (800, 400)

image12_rect = image12.get_rect()
image12_rect.topleft = (1200, 400)

image13_rect = image13.get_rect()
image13_rect.topleft = (0, 600)

image14_rect = image14.get_rect()
image14_rect.topleft = (400, 600)

image15_rect = image15.get_rect()
image15_rect.topleft = (800, 600)

image16_rect = image16.get_rect()
image16_rect.topleft = (1200, 600)


# Boucle principale du programme
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Récupération de la position du clic
            pos = pygame.mouse.get_pos()

            # Vérification si le clic a été effectué sur une image jouant un son
            if image1_rect.collidepoint(pos):
                son1.play()
            elif image2_rect.collidepoint(pos):
                son2.play()
            elif image3_rect.collidepoint(pos):
                son3.play()
            elif image4_rect.collidepoint(pos):
                son4.play()
            elif image5_rect.collidepoint(pos):
                son5.play()
            elif image6_rect.collidepoint(pos):
                son6.play()
            elif image7_rect.collidepoint(pos):
                son7.play()
            elif image8_rect.collidepoint(pos):
                son8.play()
            elif image9_rect.collidepoint(pos):
                son9.play()
            elif image10_rect.collidepoint(pos):
                son10.play()
            elif image11_rect.collidepoint(pos):
                son11.play()
            elif image12_rect.collidepoint(pos):
                son12.play()
            elif image13_rect.collidepoint(pos):
                son13.play()
            elif image14_rect.collidepoint(pos):
                son14.play()
            elif image15_rect.collidepoint(pos):
                son15.play()
            elif image16_rect.collidepoint(pos):
                son16.play()


    # Affichage des images jouant des sons avec le défilement du menu
    fenetre.blit(image1, (0, 0))
    fenetre.blit(image2, (400, 0))
    fenetre.blit(image3, (800, 0))
    fenetre.blit(image4, (1200, 0))
    fenetre.blit(image5, (0, 200))
    fenetre.blit(image6, (400, 200))
    fenetre.blit(image7, (800, 200))
    fenetre.blit(image8, (1200, 200))
    fenetre.blit(image9, (0, 400))
    fenetre.blit(image10, (400, 400))
    fenetre.blit(image11, (800, 400))
    fenetre.blit(image12, (1200, 400))
    fenetre.blit(image13, (0, 600))
    fenetre.blit(image14, (400, 600))
    fenetre.blit(image15, (800, 600))
    fenetre.blit(image16, (1200, 600))
    
    pygame.display.flip()

# Arrêt de Pygame
pygame.quit()