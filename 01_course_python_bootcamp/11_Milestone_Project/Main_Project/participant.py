from exceptions.incufficient_funds_exception import InsufficientFundsException

from abc import ABC, abstractmethod

from hand import Hand


class Participant(ABC):
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def reset_hand(self):
        self.hand.reset()

    def pay_bet(self, amount):
        if amount < 0:
            raise ValueError('Cannot pay negative amount!')

        if amount > self.balance:
            raise InsufficientFundsException('Not enough balance for the bet!')

        self.balance = self.balance - amount

    def get_paid(self, amount):
        if amount < 0:
            raise ValueError('Cannot receive negative amount!')

        self.balance = self.balance + amount

    def check_for_blackjack(self):
        hand_ranks = [card.rank for card in self.hand.current_cards]

        tens = ['10', 'J', 'Q', 'K']

        return (
            len(self.hand) == 2
            and 'A' in hand_ranks
            and any(card in hand_ranks for card in tens)
        )

    @abstractmethod
    def look_hand(self):
        pass