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
    couleurs = ["coeur", "trefle", "carreau", "pique"]
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

def determine_trick_winner(table, trump):
    winning_card = None
    winning_value = -1
    color_on_table = table[0][1] if table else None  # Color on the table if any

    for card in table:
        card_value = get_card_value(card, trump)
        if card_value > winning_value and (color_on_table is None or card[1] == color_on_table):
            winning_value = card_value
            winning_card = card

    return winning_card

def calculate_points(tricks):
    team_points = [0, 0]  # Points for Team 1 and Team 2 respectively
    for trick in tricks:
        winner = determine_trick_winner(trick, trump_card[1])  # Assuming you have a function to determine the winner of a trick
        winning_team = 0 if winner in trick[::2] else 1  # Assuming tricks are stored as [card1, card2, card3, card4] and alternate between teams

        trick_points = sum(get_card_value(card, trump_card[1]) for card in trick)
        team_points[winning_team] += trick_points

    return team_points


def display_hand(player, hand):
    print(f"{player}'s hand: {hand}")

def play_turn(player, hand, table, trump):
    print(f"{player}, it's your turn.")
    print(f"Table: {table}")
    display_hand(player, hand)



    color_on_table = table[0][1] if table else None  # Color on the table if any

    if has_color(hand, color_on_table):  # Check if player has requested color
        print(f"Play a card with color {color_on_table}.")
    else:  # Player plays a trump or any card if unable to follow the color
        print("You don't have the requested color. Play a trump card or any card.")

    chosen_card = None
    while chosen_card not in hand:
        chosen_card_input = input("Enter the card you want to play (valeur de la couleur): ")
        chosen_card = tuple(chosen_card_input.split(' de '))
        if chosen_card not in hand:
            print("Invalid card! Try again.")

    hand.remove(chosen_card)
    table.append(chosen_card)
    print(f"{player} played: {chosen_card}")
    return chosen_card

def ai_play_turn(player, hand, table, trump):
    print(f"{player}, it's your turn.")
    print(f"Table: {table}")
    display_hand(player, hand)

    color_on_table = table[0][1] if table else None

    # AI logic for choosing a card
    chosen_card = None
    if has_color(hand, color_on_table):
        for card in hand:
            if card[1] == color_on_table:
                chosen_card = card
                break
    else:
        chosen_card = random.choice(hand)

    hand.remove(chosen_card)
    table.append(chosen_card)
    print(f"{player} played: {chosen_card}")
    return chosen_card


# Modify this part in your code to compare card values and determine the winner of a trick
# after each player has played their cards.
# For instance:
# After 4 cards are played (one from each player), compare their values and determine the winner.

# Assuming 'table' contains the cards played by each player in a trick.
def determine_trick_winner(table, trump):
    winning_card = None
    winning_value = -1
    for card in table:
        card_value = get_card_value(card, trump)
        if card_value > winning_value:
            winning_value = card_value
            winning_card = card

    # The winning_card variable now holds the card that wins the trick.
    return winning_card

    # Display player's hand
    print(f"Your hand: {hand}")

    color_on_table = table[0][1] if table else None  # Color on the table if any

    if has_color(hand, color_on_table):  # Check if player has requested color
        print(f"Play a card with color {color_on_table}.")
    else:  # Player plays a trump or any card if unable to follow the color
        print("You don't have the requested color. Play a trump card or any card.")

    chosen_card = None
    while chosen_card not in hand:
        chosen_card_input = input("Enter the card you want to play (valeur de la couleur): ")
        chosen_card = tuple(chosen_card_input.split(' de '))
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
        num_players = int(input("Entrer un nombre de joueur compris (1-4): "))
        display_rules_fr()
    else:
        print("Invalid choice / Choix invalide")
        return

    if 2 <= num_players <= 4:
        players = get_player_names(num_players)
        print("Starting multiplayer game with players:", players)
        dealt_initial_cards, remaining_cards = distribute_initial_cards()

        # Initialization for multiplayer mode
        table = []
        current_player_index = 0
        rounds_played = 0
        team_points = [0, 0]

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
        for _ in range(20):
            current_player = players[current_player_index]
            current_hand = dealt_initial_cards[current_player_index]

            if current_player == players[0]:  # Human player's turn
                played_card = play_turn(current_player, current_hand, table, trump_card[1])
            else:  # AI's turn
                played_card = ai_play_turn(current_player, current_hand, table, trump_card[1])

            current_player_index = (current_player_index + 1) % num_players
            rounds_played += 1
            end_game, winner = check_end_game(team_points, rounds_played)
            if end_game:
                if winner:
                    print(f"Team {winner} wins!")
                else:
                    print("The game ends in a draw!")
                break  # End the loop as the game has ended

    if num_players == 1:
        game_mode = "2"
        players = get_player_names(2)  # Player and AI
        print("Starting game against AI with player:", players[0])

        dealt_initial_cards, remaining_cards = distribute_initial_cards()
        trump_card = select_trump_card(remaining_cards)
        table = []
        current_player_index = 0  # Initialize current_player_index here

        for _ in range(20):  # Loop through the game rounds
            current_player = players[current_player_index]
            current_hand = dealt_initial_cards[current_player_index]

            if current_player == players[0]:  # Human player's turn
                played_card = play_turn(current_player, current_hand, table, trump_card[1])
            else:  # AI's turn
                played_card = ai_play_turn(current_player, current_hand, table, trump_card[1])

            current_player_index = (current_player_index + 1) % len(players)  # Update index
            end_game, winner = check_end_game(team_points, rounds_played)
            if end_game:
                if winner:
                    print(f"Team {winner} wins!")
                else:
                    print("The game ends in a draw!")
                break  # End the loop as the game has ended

def check_end_game(team_points, rounds_played, max_rounds=20, target_score=1000):
    if rounds_played >= max_rounds:
        return True, None  # Game ends after a certain number of rounds

    for idx, points in enumerate(team_points):
        if points >= target_score:
            return True, idx + 1  # Game ends when a team reaches the target score

    return False, None  # Game continues

# Start the game
start_belote()
