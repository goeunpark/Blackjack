from Deck import Deck
from AceCard import AceCard

def play_game():
    playing_deck = Deck()
    playing_deck.shuffle()

    hand = []
    hand.append(playing_deck.draw_card())
    hand.append(playing_deck.draw_card())
    
    description = "Your hand is:\n"
    total = 0
    has_ace = False
    for card in hand:
        description += (f"{str(card)}\n")
        if not isinstance(card, AceCard):
            total += card.value
        else:
            has_ace = True
            total += 11

    if has_ace and total > 21:
        total -= 10


    print(description)
    print(f"Your total so far is {total}")

play_game()
    