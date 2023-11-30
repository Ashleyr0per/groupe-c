import random

# Function to display rules in English
def display_rules_en():
    rules_en = """
    Belote Rules:
    - The game is played with 32 cards.
    - Players form two teams.
    - The goal is to win tricks containing valuable cards.
    - ... (add more rules)
    """
    print(rules_en)

# Function to display rules in French
def display_rules_fr():
    rules_fr = """
    Règles de la Belote :
    - Le jeu se joue avec 32 cartes.
    - Les joueurs forment deux équipes.
    - Le but est de remporter des plis contenant des cartes de valeur.
    - ... (ajoutez plus de règles)
    """
    print(rules_fr)

# Function to get player names and shuffle order
def get_player_names(num_players):
    players = []
    for i in range(num_players):
        name = input(f"Enter player {i+1} name: ")
        players.append(name)

    random.shuffle(players)
    return players

# Function to initialize and distribute initial cards (5 cards per player) and a trump card
def distribute_initial_cards():
    valeurs = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    couleurs = ["[♥]", "[♦]","[♣]","[♠]"]
    cartes = [(v, c) for v in valeurs for c in couleurs]

    random.shuffle(cartes)

    players_cards = [[] for _ in range(4)]
    cards_dealt = 0

    while cards_dealt < 20:  # 5 cards per player
        for i in range(4):
            if cards_dealt >= 20 or len(players_cards[i]) >= 5:
                break
            players_cards[i].append(cartes[cards_dealt])
            cards_dealt += 1

    return players_cards, cartes[cards_dealt:]  # Return dealt cards and remaining cards

# Function to select a trump card
def select_trump_card(remaining_cards):
    random.shuffle(remaining_cards)
    return remaining_cards[0]

# Function to check if a player has a card of the requested color
def has_color(cards, color):
    for card in cards:
        if card[1] == color:
            return True
    return False

# Define point values for Trump and No Trump
trump_values = {
    "Jack": 20,
    "9": 14,
    "Ace": 11,
    "10": 10,
    "King": 4,
    "Queen": 3,
    "8": 0,
    "7": 0
}

no_trump_values = {
    "Ace": 11,
    "10": 10,
    "King": 4,
    "Queen": 3,
    "Jack": 2,
    "9": 0,
    "8": 0,
    "7": 0
}
#comparing cards during gameplay
def get_card_value(card, trump_suit):
    if card[0] == "Jack" and card[1] == trump_suit:
        return trump_values["Jack"]
    elif card[0] in trump_values:
        return trump_values[card[0]]
    else:
        return no_trump_values[card[0]]


# Function to play a turn
def play_turn(player, hand, table, trump):
    print(f"{player}, it's your turn.")
    print(f"Table: {table}")

    # Display player's hand
    print(f"Your hand: {hand}")

    color_on_table = table[0][1] if table else None  # Color on the table if any

    if has_color(hand, color_on_table):  # Check if player has requested color
        print(f"Play a card with color {color_on_table}.")
        # Player plays a card with requested color if available
        chosen_card = None
        while chosen_card not in hand:
            chosen_card = tuple(input("Enter the card you want to play (value, suit): ").split(', '))
            if chosen_card not in hand:
                print("Invalid card! Try again.")
        hand.remove(chosen_card)
        table.append(chosen_card)
        print(f"{player} played: {chosen_card}")
        return chosen_card

    else:  # Player plays a trump or any card if unable to follow the color
        print("You don't have the requested color. Play a trump card or any card.")
        # Player plays a card in the trump color or any card
        chosen_card = None
        while chosen_card not in hand:
            chosen_card = tuple(input("Enter the card you want to play (value, suit): ").split(', '))
            if chosen_card not in hand:
                print("Invalid card! Try again.")
        hand.remove(chosen_card)
        table.append(chosen_card)
        print(f"{player} played: {chosen_card}")
        return chosen_card

# Function to start the game
def start_belote():
    print("Welcome to Belote!")
    lang_choice = input("Choose 'F' for français or 'E' for english ").upper()

    if lang_choice == "E":
        num_players = int(input("Enter number of players (2-4): "))
        display_rules_en()
    elif lang_choice == "F":
        num_players = int(input("Entrer un nombre de joueur compris (2-4): "))
        display_rules_fr()
    else:
        print("Invalid choice / Choix invalide")
        return

    if 2 <= num_players <= 4:
        players = get_player_names(num_players)
        print("Starting multiplayer game with players:", players)
        dealt_initial_cards, remaining_cards = distribute_initial_cards()

        # Select and display the trump card
        trump_card = select_trump_card(remaining_cards)
        print(f"The trump card is: {trump_card[0]} of {trump_card[1]}")

        # Loop to offer players the chance to "take" the trump card or pass
        taker = None
        for i in range(len(players)):
            response = input(f"{players[i]}, do you want to take the trump card? (Y/N): ").upper()
            if response == "Y":
                taker = players[i]
                break

        if taker:
            print(f"{taker} took the trump card!")
            # Players receive additional cards after the trump is taken
            additional_cards = remaining_cards[:5]
            remaining_cards = remaining_cards[5:]

            # Distribute additional cards (2 to taker, 3 to others)
            for i in range(num_players):
                if players[i] == taker:
                    dealt_initial_cards[i] += additional_cards[:2]
                else:
                    dealt_initial_cards[i] += additional_cards[2:5]

        else:
            print("No one took the trump card. Redistributing cards...")

            # Redistribute cards if no one takes the trump card
            remaining_cards.extend([card for hand in dealt_initial_cards for card in hand])
            random.shuffle(remaining_cards)

        # Start playing the game
        current_player_index = players.index(taker) if taker else 0
        table = []  # Cards on the table
        for _ in range(20):  # 20 turns in total
            current_player = players[current_player_index]
            current_hand = dealt_initial_cards[current_player_index]

            played_card = play_turn(current_player, current_hand, table, trump_card[1])

            # Move to the next player
            current_player_index = (current_player_index + 1) % num_players

    elif num_players == 1:
        game_mode = "2"  # Set to play against AI automatically if only one player
        players = get_player_names(1)  # Set 1 player for AI
        print("Starting game against AI with player:", players[0])
        # Implement AI game logic here
    else:
        print("Invalid choice. Exiting.")

# Start the game
start_belote()
