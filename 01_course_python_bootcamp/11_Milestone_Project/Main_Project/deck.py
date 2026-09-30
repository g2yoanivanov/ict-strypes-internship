from settings import suits, ranks
from settings import DECKS_NUMBER

from card import Card

import random

class Deck:
    """
    Deck for the Blackjack game. One Blackjack deck contains general.DECKS_NUMBER decks of playing cards.
    Total of (general.DECKSNUMBER * 52) cards.
    """
    def __init__(self):
        self.all_cards = []

        for _ in range(DECKS_NUMBER):
            for suit in suits:
                for rank in ranks:
                    card = Card(suit, rank)
                    self.all_cards.append(card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def reshuffle(self, removed_cards):
        self.all_cards.extend(removed_cards)
        self.shuffle()

    def deal_one(self):
        return self.all_cards.pop()

    def __len__(self):
        return len(self.all_cards)