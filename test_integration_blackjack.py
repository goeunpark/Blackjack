import pytest
from Deck import Deck  # from Deck.py, import Deck class
from Card import Card  # from Card.py, import Card class
from FaceCard import FaceCard
from AceCard import AceCard

def test_deck_has_52_cards_as_default():
    new_deck = Deck()
    assert len(new_deck.cards) == 52
    assert type(new_deck.cards[0]) == Card

def test_create_face_card():
    new_face_card = FaceCard('Jack', 'Spades')
    assert new_face_card.face == 'Jack'
    assert new_face_card.value == 10
    assert new_face_card.suit == 'Spades'

def test_create_ace_card():
    new_ace_card = AceCard('Hearts')
    assert new_ace_card.value == (1, 11)
    assert new_ace_card.suit == 'Hearts'

def test_deck_stringify_returns_all_cards():
    actual = "Ace of Hearts, 2 of Heats, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, Jack of Hearts, Queen of Hearts, King of Hearts, Ace of Spades, 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 9 of Spades, 10 of Spades, Jack of Spades, Queen of Spades, King of Spades, Ace of Diamonds, 2 of Diamonds, 3 of Diamonds, 4 of Diamonds, 5 of Diamonds, 6 of Diamonds, 7 of Diamonds, 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, Jack of Diamonds, Queen of Diamonds, King of Diamonds, Ace of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, Jack of Clubs, Queen of Clubs, King of Clubs, "
    new_deck_str = str(Deck())

    assert type(new_deck_str) == str
    assert new_deck_str == actual
