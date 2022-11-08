import random

from Card import Card  # from Card.py, import Card class
from FaceCard import FaceCard
from AceCard import AceCard

SUITS = ["Hearts", "Spades", "Diamonds", "Clubs"]
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
FACE_VALUES = ["Jack", "Queen", "King"]

class Deck():
    def __init__(self, cards = None):
        if cards is None:
            self.cards = self.create_52_deck()
        else:
            self.cards = cards

    def __str__(self): # stringify
        description = ""

        for card in self.cards:
            description += (f"{card.value} of {card.suit}, ")
        
        return description

    def create_52_deck(self):
        deck_of_cards = []
        for suit in SUITS: 
            for value in VALUES:
                new_card = Card(value, suit)
                deck_of_cards.append(new_card)
            for face_type in FACE_VALUES:
                new_card = FaceCard(face_type, suit)
                deck_of_cards.append(new_card)
            new_card = AceCard(suit)
            deck_of_cards.append(new_card)

        return deck_of_cards

    def shuffle(self):
        random.shuffle(self.cards)
        # NOT self.cards.random()
        return self.cards


    def draw_card(self):
        # engineering decision: will not 
        drawn_card = self.cards.pop() # <-- WHY IS THIS POPPING OUT RANDOMLY INSTEAD OF AT THE END? 
        return drawn_card

#a_small_deck = Deck()
#print(str(a_small_deck))

#print("__________________")
#a_small_deck.shuffle()
#print(str(a_small_deck))

#print("__________________")
#print(a_small_deck.draw_card().suit)
#print(a_small_deck.draw_card().value)
