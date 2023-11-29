"""
import random


def ajoute_nb_alea(maListe):
    nbAlea = random.randint(-10,10)
    for i in range(len(maListe)) : 
        maListe[i]+= nbAlea
    return maListe

#programme principal
maListe = [7,3,8,4,5,1,9,10,2,6]
print (maListe)
maListe = ajoute_nb_alea(maListe)
print (maListe)
"""
"""
# Code pour français
def francais():
    print("Vous avez choisi français")
    # Ajout du code

# Code pour anglais
def english():
    print("You chose english")
    # Ajout du code 


#L'utilateur choisi la langue qu'il ou elle souhaite utiliser entre français et english
def choix_langue():
    print("Choisissez votre langue")
    while True:
        user_input  = input("Choisir 'F' pour français ou 'E' for english ").upper()
        if user_input  == 'F':
            francais()
            break
        elif user_input  == 'E':
            english()
            break
        else:
            print("Réponse invalide. Choisir entre 'F' ou 'E'.")

# Apelle de la fonction choix_langue
choix_langue()
"""
"""
def francais():
    print("Vous avez choisi français")
    # Ajout du code

def english():
    print("You chose english")
    # Ajout du code 

def choix_langue():
    print("Choisissez votre langue")
    while True:
        user_input = input("Choisir 'F' pour français ou 'E' for english ").strip().upper()
        if user_input == 'F':
            francais()
            break
        elif user_input == 'E':
            english()
            break
        else:
            print("Réponse invalide. Choisir entre 'F' ou 'E'.")

# Appel de la fonction choix_langue
choix_langue()
"""



