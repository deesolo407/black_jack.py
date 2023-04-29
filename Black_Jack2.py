import random

# Define the suits and card values
suits = ['♠', '♡', '♢', '♣']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Define the card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.value == '10':
            return f"┌─────┐\n|{self.value}{self.suit} |\n|     |\n|{self.suit}{self.value} |\n└─────┘"
        else:
            return f"┌─────┐\n|{self.value}{self.suit}  |\n|     |\n|  {self.suit}{self.value}|\n└─────┘"

# Define the deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

# Define the player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.deal()
        self.hand.append(card)

    def show_hand(self, show_all=False):
        print(f"{self.name}'s hand:")
        if show_all:
            for card in self.hand:
                print(card)
        else:
            print(self.hand[0])
            print("┌─────┐")
            print("|     |")
            print("|  ?  |")
            print("|     |")
            print("└─────┘")

    def get_hand_value(self):
        hand_value = 0
        num_aces = 0
        for card in self.hand:
            if card.value == 'A':
                num_aces += 1
                hand_value += 11
            elif card.value in ['K', 'Q', 'J']:
                hand_value += 10
            else:
                hand_value += int(card.value)
        
        while num_aces > 0 and hand_value > 21:
            hand_value -= 10
            num_aces -= 1
        
        return hand_value

# Define the game class
class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        for i in range(2):
            self.player.draw_card(self.deck)
            self.dealer.draw_card(self.deck)

    def player_turn(self):
        while self.player.get_hand_value() < 21:
            self.player.show_hand()
            action = input("What would you like to do? Hit (h), Stand (s), or Double Down (dd)? ")
            if action.lower() == 'h':
                self.player.draw_card(self.deck)
            elif action.lower() == 's':
                break
            elif action.lower() == 'dd':
                self.player.draw_card(self.deck)
                break

    def dealer_turn(self):
        while self.dealer.get_hand_value() < 17:
            self.dealer.draw_card(self.deck)

    def show_final_hands(self
