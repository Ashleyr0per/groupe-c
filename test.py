import random

# Initialisation des cartes
valeurs = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
cartes =[(v, c) for v in valeurs for c in couleurs]

# Mélange des cartes
random.shuffle(cartes)


# Distribution des cartes aux joueurs
joueurs = [[], [], [], []]
for i in range(len(cartes)):
    carte = cartes[i]
    joueurs[i % 4].append(carte)  # % permet d'obtenir le reste de la division i/4 donc (0,1,2,3, etc),  permet de distribuer les cartes alternativement
                                          

# Affichage des mains des joueurs
for i in range(len(joueurs)):
    numero_joueur = i + 1
    representation_cartes = ""
    for valeur, couleur in joueurs[i]:
        representation_cartes += f'{valeur} de {couleur}, ' 
    
    representation_cartes = representation_cartes[:-2]     # Supprime les deux derniers caractères (virgule à la fin)
    print(f"Joueur {numero_joueur}: {representation_cartes}") 

#affichage de la carte atout

carte_atout = random.choice(cartes)
print(f"\nL'atout est : {carte_atout[0]} de {carte_atout[1]}")






