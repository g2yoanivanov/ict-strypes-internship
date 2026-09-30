class Hand:
    def __init__(self):
        self.current_cards = []
        self.hand_value = 0

    def reset(self):
        self.current_cards = []
        self.hand_value = 0

    def add_card(self, card):
        self.current_cards.append(card)

        if card.rank != 'A':
            self.hand_value = self.hand_value + card.value

        else:
            print(card.value)
            if self.hand_value + card.value[1] <= 21:
                self.hand_value = self.hand_value + card.value[1]

            else:
                self.hand_value = self.hand_value + card.value[0]

    def recalculate_hand_value(self):
        pass

    def __len__(self):
        return len(self.current_cards)

    def __str__(self):
        return ' '.join(str(card) for card in self.current_cards)