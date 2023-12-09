import random

# Fonction pour afficher les regles en anglais
def affichage_regle_en():
    regle_en = print(''' The goal of belote game :

        Belote is a game of contract. The team that "takes" the contract must reach 82 points minimum to win. If this total is reached,
        each team scores the points it has made. If the team fails to reach the 82 points, it does not score a point, the 162 points will
        be awarded to the opponents. The total number of possible points (cards and ten der) in the folds is 162 points. The game ends
        when one of the team reaches a minimum of 501 points. If both teams exceed 501 points, the team with the highest score wins the match.

        Value and order of Belote cards :
        Trump	No Trump
        Jack : 20 points  	Ace : 11 points
        9 : 14 points	    10 : 10 points
        Ace : 11 points	    King : 4 points
        10 : 10 points	    Queen : 3 points
        King : 4 points	    Jack : 2 points
        Queen : 3 points	9 : 0 point
        8 : 0 point	        8 : 0 point
        7 : 0 point	        7 : 0 point

        The distribution of cards :
        The cards are distributed in two phases. In the first phase, each joueur receives 5 cards. A carte in the middle of
        the table is then placed face up in the middle of the table. The carte is considered the color of the atout.
        The first joueur located after the dealer choose to "take" or not take the atout carte. If the joueur does not take,
        it is up to the next joueur to take the carte or not. If, in the first round, one of the joueurs decides to take the atout, the game begins.
        If none of the joueurs want to take on, then the first joueur may choose to announce another color, different from the carte on the field.
        If he does not say anything, the next joueur can choose his asset color. If one joueur chooses the color, the game can begin.

        If no joueur takes the first and second turns, the cards are redistributed.

        When a joueur decides to take, he receives 2 additional cards and the other joueurs receive 3 additional cards. All joueurs should have 8 cards each.

        How to play the game:
        The joueur to the dealer s left begins the turn with a carte of his choice. Each joueur must play the carte with the requested color.
        If a joueur can not provide a carte of that color, he must necessarily play a carte in the atout color. If he does not have an asset, he can play another carte in another color.

        In some cases, it is possible not to play the atout. If a joueur s partner carte is the strongest on the table and the joueur does not have the color to follow.
        The joueur who wins the turn plays the first carte of the next turn. The strengths are always stronger than the others.

        When two joueurs cut, the second joueur must necessarily overtake, that is, provide a stronger atout than the one already on the table.
        If he does not have a stronger asset, he must still provide an asset if he has one.

        How to count the points at the Belote ?
        The team that took the contract must collect more points than the other team and must have at least 82 points. The last fold is worth 10 extra points ("the 10 of der").
        For the 32 cards, we have 152 points. And add the "10 of der or 162 points in total.
        If the attacking team reaches a minimum of 82 points, each team scores the points it has obtained.
        ''')
    print(regle_en)

# Fonction pour afficher les regle en français
def affichage_regle_fr():
    regle_fr = '''
    Le but du jeu de belote :

    La Belote est un jeu de contrat. L'équipe qui "prend" le contrat doit atteindre un minimum de 82 points pour gagner. Si ce total est atteint,
    chaque équipe marque les points qu'elle a obtenus. Si l'équipe ne parvient pas à atteindre les 82 points, elle ne marque pas de point, les 162 points
    seront attribués aux adversaires. Le nombre total de points possibles (cartes et dix de der) dans les plis est de 162 points. Le jeu se termine
    lorsqu'une des équipes atteint un minimum de 501 points. Si les deux équipes dépassent 501 points, l'équipe ayant le score le plus élevé remporte la partie.

    Valeur et ordre des cartes de Belote :
    Atout	 Sans Atout
    Valet : 20 points	    As : 11 points
    9 : 14 points	        10 : 10 points
    As : 11 points	        Roi : 4 points
    10 : 10 points	        Dame : 3 points
    Roi : 4 points	        Valet : 2 points
    Dame : 3 points	        9 : 0 point
    8 : 0 point	            8 : 0 point
    7 : 0 point	            7 : 0 point

    La distribution des cartes :
    Les cartes sont distribuées en deux phases. Dans la première phase, chaque joueur reçoit 5 cartes. Une carte est ensuite placée face visible au milieu de
    la table. La carte est considérée comme la couleur de l'atout. Le premier joueur situé après le donneur choisit de "prendre" ou de ne pas prendre la carte d'atout.
    Si le joueur ne prend pas, c'est au joueur suivant de prendre la carte ou non. Si, lors du premier tour, l'un des joueurs décide de prendre l'atout, le jeu commence.
    Si aucun des joueurs ne souhaite prendre, alors le premier joueur peut choisir d'annoncer une autre couleur, différente de la carte sur le terrain.
    S'il ne dit rien, le joueur suivant peut choisir sa couleur d'atout. Si un joueur choisit la couleur, le jeu peut commencer.

    Si aucun joueur ne prend aux premier et second tours, les cartes sont redistribuées.

    Lorsqu'un joueur décide de prendre, il reçoit 2 cartes supplémentaires et les autres joueurs reçoivent 3 cartes supplémentaires. Tous les joueurs doivent avoir 8 cartes chacun.

    Comment jouer au jeu :
    Le joueur à gauche du donneur commence le tour avec une carte de son choix. Chaque joueur doit jouer la carte de la couleur demandée.
    Si un joueur ne peut pas fournir une carte de cette couleur, il doit nécessairement jouer une carte dans la couleur de l'atout. S'il n'a pas d'atout,
    il peut jouer une autre carte dans une autre couleur.

    Dans certains cas, il est possible de ne pas jouer l'atout. Si la carte partenaire d'un joueur est la plus forte sur la table et que le joueur n'a pas la couleur pour suivre.
    Le joueur qui remporte le pli joue la première carte du tour suivant. Les atouts sont toujours plus forts que les autres.

    Lorsque deux joueurs coupent, le deuxième joueur doit nécessairement surcouper, c'est-à-dire fournir un atout plus fort que celui déjà sur la table.
    S'il n'a pas d'atout plus fort, il doit quand même fournir un atout s'il en a un.

    Comment compter les points à la Belote ?
    L'équipe qui a pris le contrat doit récolter plus de points que l'autre équipe et doit avoir au moins 82 points. Le dernier pli vaut 10 points supplémentaires (le "10 de der").
    Pour les 32 cartes, nous avons 152 points. Et ajoutez le "10 de der" ou 162 points au total.
    Si l'équipe attaquante atteint un minimum de 82 points, chaque équipe marque les points qu'elle a obtenus.
    '''
    print(regle_fr)

# Fonction pour avoir le nom des joueurs et les mélanger
def avoir_nom_joueurs(num_joueurs):
    joueurs = []
    for i in range(num_joueurs):
        nom = input(f"Entrer votre {i+1} nom: ")
        joueurs.append(nom)

    random.shuffle(joueurs)
    return joueurs

# FOnction pour initialiser et distribuer les cartes et l'atout
def distribution_initial_cartes():
    valeurs = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    couleurs = ["coeur", "trefle", "carreau", "pique"]
    cartes = [(v, c) for v in valeurs for c in couleurs]

    random.shuffle(cartes)

    cartes_joueurs = [[] for _ in range(4)]
    cartes_donner = 0

    while cartes_donner < 20:  # 5 cartes par joueurs
        for i in range(4):
            if cartes_donner >= 20 or len(cartes_joueurs[i]) >= 5:
                break
            cartes_joueurs[i].append(cartes[cartes_donner])
            cartes_donner += 1

    return cartes_joueurs, cartes[cartes_donner:]  # Return les cartes_donner et les cartes restantes

# Fonction pour prendre l'atout
def select_atout(cartes_restantes):
    random.shuffle(cartes_restantes)
    return cartes_restantes[0]

# Fonction pour verifier si le joueur a une cartes correspondant a la couleur
def joueur_a_couleur(cartes, couleur):
    for carte in cartes:
        if carte[1] == couleur:
            return True
    return False

#  atout and Non atout
valeur_atout = {
    "Valet": 20,
    "9": 14,
    "As": 11,
    "10": 10,
    "Roi": 4,
    "Dame": 3,
    "8": 0,
    "7": 0
}

valeur_non_atout = {
    "As": 11,
    "10": 10,
    "Roi": 4,
    "Dame": 3,
    "Valet": 2,
    "9": 0,
    "8": 0,
    "7": 0
}
#comparing cards during gameplay
def get_valeur_carte(carte, atout):
    if carte[0] == "Valet" and carte[1] == atout:
        return valeur_atout["Valet"]
    elif carte[0] in valeur_atout:
        return valeur_atout[carte[0]]
    else:
        return valeur_non_atout[carte[0]]

def calculate_points(tours):
    points_equipe = [0, 0]  # Points pour equipe 1 et 2
    for tour in tours:
        gagnant = determine_trick_gagnant(tour, atout[1])
        equipe_gagnante = 0 if gagnant in tour[::2] else 1

        points_tour = sum(get_valeur_carte(carte, atout[1]) for carte in tour)
        points_equipe[equipe_gagnante] += points_tour

    return points_equipe


def display_hand(joueur, main):
    print(f"main du {joueur}'s : {main}")

def tour_jeu(joueur, main, table, atout):
    print(f"{joueur}, c'est ton tour.")
    print(f"Table: {table}")
    display_hand(joueur, main)



    couleur_de_table = table[0][1] if table else None

    if joueur_a_couleur(main, couleur_de_table):  # Verifier si le joueur a choisi un atout
        print(f"Jouez une carte avec la meme couleur {couleur_de_table}.")
    else:  # Le joueur joue un atout ou n'importe quelle carte s'il est incapable de suivre la couleur
        print("Si vous n'avez pas la même couleur choisi jouez un atout ou une autre carte ")

    carte_choisi = None
    while carte_choisi not in main:
        input_carte_choisi = input("Entrez la carte que vous souhaitez jouer (valeur de la couleur): ")
        carte_choisi = tuple(input_carte_choisi.split(' de '))
        if carte_choisi not in main:
            print("Carte invalide! Essayez à nouveau")

    main.remove(carte_choisi)
    table.append(carte_choisi)
    print(f"{joueur} played: {carte_choisi}")
    return carte_choisi

def tour_jeu_ia(joueur, main, table, atout):
    print(f"{joueur}, c'est votre tour.")
    print(f"Table: {table}")
    display_hand(joueur, main)

    couleur_de_table = table[0][1] if table else None

    # Logique de l'IA pour choisir une carte
    carte_choisi = None
    if joueur_a_couleur(main, couleur_de_table):
        for carte in main:
            if carte[1] == couleur_de_table:
                carte_choisi = carte
                break
    else:
        carte_choisi = random.choice(main)

    main.remove(carte_choisi)
    table.append(carte_choisi)
    print(f"{joueur} played: {carte_choisi}")
    return carte_choisi


#En supposant que 'table' contient les cartes jouées par chaque joueur dans un tour
def determine_trick_gagnant(table, atout):
    carte_gagnante = None
    valeur_gagnante = -1
    couleur_de_table = table[0][1] if table else None

    for carte in table:
        card_value = get_valeur_carte(carte, atout)
        if card_value > valeur_gagnante and (couleur_de_table is None or carte[1] == couleur_de_table):
            valeur_gagnante = card_value
            carte_gagnante = carte

    return carte_gagnante

    # Montrer le main du joueur
    print(f"Votre main: {main}")

    couleur_de_table = table[0][1] if table else None

    if joueur_a_couleur(main, couleur_de_table):
        print(f"Play a carte with color {couleur_de_table}.")
    else:
        print("Si vous n'avez pas la même couleur choisi jouez un atout ou une autre carte.")

    carte_choisi = None
    while carte_choisi not in main:
        input_carte_choisi = input("Entrez la carte que vous souhaitez jouer (valeur de la couleur): ")
        carte_choisi = tuple(input_carte_choisi.split(' de '))
        if carte_choisi not in main:
            print("Carte invalide! Essayez à nouveau.")

    main.remove(carte_choisi)
    table.append(carte_choisi)
    print(f"{joueur} played: {carte_choisi}")
    return carte_choisi


# Fonction du jeu
def start_jeu():
    print("Bienvenue!")
    lang_choice = input("Choose 'F' for français or 'E' for english ").upper()

    if lang_choice == "E":
        nb_joueur = int(input("Enter number of joueurs (1-4): "))
        affichage_regle_en()
    elif lang_choice == "F":
        nb_joueur = int(input("Entrer un nombre de joueur compris (1-4): "))
        affichage_regle_fr()
    else:
        print("Invalid choice / Choix invalide")
        return

    if 2 <= nb_joueur <= 4:
        joueurs = avoir_nom_joueurs(nb_joueur)
        print("Commencer une partie multijoueur avec les joueurs :", joueurs)
        carte_donner, carte_restantes = distribution_initial_cartes()

        # Initialization mode multijoueurs
        table = []
        index_joueur_actuelle = 0
        tour_jouer = 0
        points_equipe = [0, 0]


        atout = select_atout(carte_restantes)
        print(f"Votre atout est {atout[0]} de {atout[1]}")

        # Loop pour offrir aux joueurs la possibilité de "prendre" la carte d'atout ou de passer"
        preneur = None
        for i in range(len(joueurs)):
            reponse = input(f"{joueurs[i]}, Voulez_vous prendre la carte ? (Y/N): ").upper()
            if reponse == "Y":
                preneur = joueurs[i]
                break

        if preneur:
            print(f"{preneur} a pris la carte!")

            cartes_aditonnel = carte_restantes[:5]
            carte_restantes = carte_restantes[5:]


            for i in range(nb_joueur):
                if joueurs[i] == preneur:
                    carte_donner[i] += cartes_aditonnel[:2]
                else:
                    carte_donner[i] += cartes_aditonnel[2:5]

        else:
            print("Persone n'a pris une carte. Redistribution des cartes.")


            carte_restantes.extend([carte for main in carte_donner for carte in main])
            random.shuffle(carte_restantes)

        for _ in range(20):
            joueur_actu = joueurs[index_joueur_actuelle]
            main_actu = carte_donner[index_joueur_actuelle]

            if joueur_actu == joueurs[0]:  #tour joueur
                carte_jouer = tour_jeu(joueur_actu, main_actu, table, atout[1])
            else:  # tour IA
                carte_jouer = tour_jeu_ia (joueur_actu, main_actu, table, atout[1])

            index_joueur_actuelle = (index_joueur_actuelle + 1) % nb_joueur
            tour_jouer += 1
            end_jeu, gagnant = verifier_end_jeu(points_equipe, tour_jouer)
            if end_jeu:
                if gagnant:
                    print(f"Equipe {gagnant} gagne!")
                else:
                    print("La partie se termine sur un match nul!")
                break

    if nb_joueur == 1:
        jeu_mode = "2"
        joueurs = avoir_nom_joueurs(2)  # Joueur et IA
        print("Commencer la partie contre l'IA avec le joueur :", joueurs[0])

        carte_donner, carte_restantes = distribution_initial_cartes()
        atout = select_atout(carte_restantes)
        table = []
        index_joueur_actuelle = 0

        for _ in range(20):
            joueur_actu = joueurs[index_joueur_actuelle]
            main_actu = carte_donner[index_joueur_actuelle]
            points_equipe = [0, 0]
            tour_jouer = 0

            if joueur_actu == joueurs[0]:
                carte_jouer = tour_jeu(joueur_actu, main_actu, table, atout[1])
            else:
                carte_jouer = tour_jeu_ia (joueur_actu, main_actu, table, atout[1])

            index_joueur_actuelle = (index_joueur_actuelle + 1) % len(joueurs)
            end_jeu, gagnant = verifier_end_jeu(points_equipe, tour_jouer)
            if end_jeu:
                if gagnant:
                    print(f"Team {gagnant} wins!")
                else:
                    print("The game ends in a draw!")
                break

def verifier_end_jeu(points_equipe, tour_jouer, tour_max=20, score_cible=1000):
    if tour_jouer >= tour_max:
        return True, None

    for idx, points in enumerate(points_equipe):
        if points >= score_cible:
            return True, idx + 1

    return False, None


# Start the game
start_jeu()
