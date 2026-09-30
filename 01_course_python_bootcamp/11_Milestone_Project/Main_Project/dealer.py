from participant import Participant
from hand import Hand

import settings


class Dealer(Participant):
    def __init__(self):
        super().__init__(settings.CASINO_FUNDS)

    def look_hand(self, player_hit):
        if len(self.hand) == 2 and not player_hit:
            return f'{str(self.hand.current_cards[0])} ?'

        return self.hand
