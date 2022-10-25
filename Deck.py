from Card import Card # from Card.py, import Card class

SUITS = ["Hearts", "Spades", "Diamonds", "Clubs"]
VALUES = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

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

        return deck_of_cards

a_small_deck = Deck()
print(str(a_small_deck))