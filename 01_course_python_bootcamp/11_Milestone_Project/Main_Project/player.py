from participant import Participant
from hand import Hand


class Player(Participant):
    def __init__(self, name, balance):
        super().__init__(balance)
        self.name = name
        self.stand = False

        self.statistics = {
            'wins': 0,
            'loses': 0,
            'busts': 0,
            'ties': 0,
            'surrenders': 0,
            'winnings': 0
        }

    def look_hand(self):
        return self.hand

    def __str__(self):
        return f'Player: {self.name}\n{self.statistics}'