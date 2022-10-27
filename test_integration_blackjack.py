import pytest
from Deck import Deck #from Deck.py, import Deck class
from Card import Card # from Card.py, import Card class
from FaceCard import FaceCard
from AceCard import AceCard


# @pytest.mark.integration_test
def test_deck_has_52_cards_as_default():
    new_deck = Deck()
    assert len(new_deck.cards) == 52
    assert type(new_deck.cards[0]) == Card


# if you have a problem getting pytest to work:
# def test_should_be_true():
#     assert True