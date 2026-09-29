from card import Card
from deck import Deck
from player import Player

def deal_cards(player1, player2, deck):
    cards_per_person = len(deck) // 2

    for _ in range(cards_per_person):
            card1 = deck.deal_one()
            card2 = deck.deal_one()
    
            player1.add_cards(card1)
            player2.add_cards(card2)


def main():
    deck = Deck()
    deck.shuffle()

    player1 = Player('Yoan')
    player2 = Player('Tsvetan')

    deal_cards(player1, player2, deck)

    playing = True

    rounds = 0

    while playing:
        rounds = rounds + 1
        print(f'Round {rounds}')

        if len(player1.all_cards) == 0:
            print(f'{player1.name} ran out of cards!')
            print(f'{player2.name.upper()} WINS!')
            playing = False
            break

        if len(player2.all_cards) == 0:
            (f'{player2.name} ran out of cards!')
            (f'{player1.name.upper()} WINS!')
            playing = False
            break

        round_cards_player1 = []
        round_cards_player2 = []

        round_cards_player1.append(player1.remove_one_card())
        round_cards_player2.append(player2.remove_one_card())

        at_war = True

        while at_war:
            if round_cards_player1[-1].value > round_cards_player2[-1].value:
                player1.add_cards(round_cards_player1)
                player1.add_cards(round_cards_player2)

                at_war = False

            elif round_cards_player1[-1].value < round_cards_player2[-1].value:
                player2.add_cards(round_cards_player2)
                player2.add_cards(round_cards_player1)

                at_war = False

            else:
                print('WAR!')

                if len(player1.all_cards) < 4:
                    print(f'{player1.name} does not have enough cards!')
                    print(f'{player2.name.upper()} WINS!')
                    playing = False
                    break
            
                if len(player2.all_cards) < 4:
                    print(f'{player2.name} does not have enough cards!')
                    print(f'{player1.name.upper()} WINS!')
                    playing = False
                    break

                for _ in range(3):
                    round_cards_player1.append(player1.remove_one_card())
                    round_cards_player2.append(player2.remove_one_card())


if __name__ == '__main__':
    main()