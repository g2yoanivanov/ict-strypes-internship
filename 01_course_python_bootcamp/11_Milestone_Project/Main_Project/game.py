from deck import Deck
from player import Player
from dealer import Dealer
from hand import Hand

from exceptions.incufficient_funds_exception import InsufficientFundsException

import settings

def get_starting_balance():
    while True:
        try:
            balance = int(input('Enter starting balance: '))

            if balance <= 0:
                raise ValueError

        except ValueError:
            print('Starting balance must be a positive number!')

        else:
            print()
            break

    return balance


def place_bet(balance):
    while True:
        try:
            if balance <= 0:
                raise InsufficientFundsException()

            bet = int(input('Place your bet: '))

            if bet > balance:
                raise InsufficientFundsException()

            if bet <= 0:
                raise ValueError

        except ValueError:
            print('Bet must be a positive number!')

        except InsufficientFundsException:
            print('Not enough balance to place this bet!')

        except Exception as e:
            print(e)
        
        else:
            print()
            break

    return bet


def dealer_turn(deck, dealer, removed_cards, player):
    dealer_bust = False
    direct_stand = True

    while dealer.hand.hand_value <= 16:
        deal_card(deck, dealer, removed_cards)
        direct_stand = False
        display_current_hands(player, dealer)

    # HIT ON SOFT 17
    if dealer.hand.hand_value == 17 and 'A' in [card for card in dealer.hand.current_cards]:
        deal_card(deck, dealer, removed_cards)
        direct_stand = False
        display_current_hands(player, dealer)

    if dealer.hand.hand_value > 21:
        dealer_bust = True

    if direct_stand:
        display_current_hands(player, dealer)

    return dealer_bust


def proceed():
    while True:
        proceed = input('Game is ready to start. Proceed? (yes/no): ')

        proceed = proceed.lower()

        if proceed == 'yes':
            return True

        if proceed == 'no':
            return False

        print('Invalid answer!')


def play_again(player):
    print(f'New balance: {player.balance}')
    while True:
        proceed = input('Play again? (yes/no): ')
        print()

        proceed = proceed.lower()

        if proceed == 'yes':
            return True

        if proceed == 'no':
            return False

        print('Invalid answer!')


def deal_card(deck, participant, removed_cards):
    new_card = deck.deal_one()
    participant.hand.add_card(new_card)
    removed_cards.append(new_card)


def display_options(first_turn):
    print('Options:')
    print('1. Hit')
    print('2. Stand')

    if first_turn:
        print('3. Double Down (dd)')
        print('4. Surrender (ff)')


def display_current_hands(player, dealer, ):
    print(f"Player's hand: {player.look_hand()}  Value: {player.hand.hand_value}")
    print(f"Dealer's hand: {dealer.look_hand(player.stand)}") 
    print() 


def display_goodbye_message():
    print()
    print('Thank you for coming! Goodbye!')
    print()


def surrender(player, dealer, bet):
    print('PLAYER SURRENDERED!')
    
    return_bet = bet // 2
    dealer_win_bet = bet - return_bet

    dealer.pay_bet(return_bet)
    dealer.get_paid(dealer_win_bet)

    player.get_paid(return_bet)

    player.statistics['surrenders'] += 1


def tie(player, dealer, bet):
    print(f'{player.name.upper()} TIES WITH DEALER!')
    print(f"Dealer's hand value: {dealer.hand.hand_value}")
    player.statistics['ties'] += 1
    dealer.pay_bet(bet)
    player.get_paid(bet)


def player_win(player, dealer, bet):
    print(f'{player.name.upper()} WINS OVER DEALER!')
    print(f"Dealer's hand value: {dealer.hand.hand_value}")
    player.statistics['wins'] += 1
    player.statistics['winnings'] += bet
    dealer.pay_bet(bet)
    player.get_paid(bet)


def dealer_win(player, dealer):
    print(f'DEALER WINS OVER {player.name.upper()}')
    print(f"Dealer's hand value: {dealer.hand.hand_value}")
    player.statistics['loses'] += 1


def main():
    while True:
        print('Welcome to Black Jack')
        print()
        print('(Enter "q" to quit):')
        name = input('Enter your name: ')

        if name == 'q':
            display_goodbye_message()
            break

        balance = get_starting_balance()
        
        player = Player(name, balance)
        player.hand = Hand()

        dealer = Dealer()
        dealer.hand = Hand()

        deck = Deck()
        deck.shuffle()

        removed_cards = []

        if not proceed():
            display_goodbye_message()
            continue 

        playing = True
        while playing:
            print()
            print('NEW GAME!')

            player.reset_hand()
            dealer.reset_hand()

            bet = place_bet(player.balance)
            return_bet = bet
            player.pay_bet(bet)
            dealer.get_paid(bet)

            if len(deck) <= settings.TOTAL_CARDS * settings.SHUFFLE_PERCENT:
                deck.reshuffle(removed_cards)
                removed_cards = []
                print('DECK RESHUFFLED!')

            # Deal cards
            for _ in range(2):
                player_card = deck.deal_one()
                player.hand.add_card(player_card)

                dealer_card = deck.deal_one()
                dealer.hand.add_card(dealer_card)

                removed_cards.extend([player_card, dealer_card])

            display_current_hands(player, dealer)

            if dealer.check_for_blackjack() and player.check_for_blackjack():
                print('2 BLACKJACKS!')
                tie(player, dealer, return_bet)
                break

            elif dealer.check_for_blackjack():
                print('DEALER HAS A BLACKJACK')
                dealer_win(player, dealer)
                break

            elif player.check_for_blackjack():
                print(f'{player.name.upper()} HAS A BLACKJACK!')
                player_win(player, dealer, bet)
                break
            
            player_turn = True
            first_turn = True
            lost = False # player_bust, dealer_bust
            while player_turn:
                print('(Eneter 0 for help)')
                choice = input("Player's choice: ")

                if choice == '0':
                    display_options()
                    continue

                if not first_turn and choice in ['ff', 'db']:
                    print('You cannot do that now...')
                    continue

                if choice not in ['hit', 'stand', 'ff', 'db']:
                    print('Invalid choice...')
                    continue

                if first_turn:
                    first_turn = False

                if choice == 'hit':
                    deal_card(deck, player, removed_cards)

                    display_current_hands(player, dealer)

                    if player.hand.hand_value > 21:
                        print('PLAYER BUSTED!')

                        dealer_win(player, dealer)
                        player.statistics['busts'] += 1

                        player_turn = False
                        lost = True
                        break

                    continue

                if choice == 'ff':
                    surrender(player, dealer, bet)

                    player_turn = False
                    break

                if choice == 'db':
                    player.pay_bet(bet)
                    dealer.get_paid(bet)
                    return_bet = (return_bet + bet) * 2

                    deal_card(deck, player, removed_cards)

                    display_current_hands(player, dealer)

                    if player.hand.hand_value > 21:
                        print('PLAYER BUSTED!')

                        dealer_win(player, dealer)
                        player.statistics['busts'] += 1

                        player_turn = False
                        lost = True
                        break

                    if dealer_turn(deck, dealer, removed_cards, player):
                        print('DEALER BUSTED!')

                        player_win(player, dealer, return_bet)

                        lost = True
                    break

                if choice == 'stand':
                    player.stand = True
                    if dealer_turn(deck, dealer, removed_cards, player):
                        print('DEALER BUSTED!')

                        player_win(player, dealer, return_bet * 2)

                        lost = True
                    break

            if not lost:
                player_hand_value = player.hand.hand_value
                dealer_hand_value = dealer.hand.hand_value

                if player_hand_value > dealer_hand_value:
                    player_win(player, dealer, return_bet * 2)  
                    

                elif player_hand_value < dealer_hand_value:
                    dealer_win(player, dealer)

                else:
                    tie(player, dealer, return_bet)
                
            if not play_again(player):
                playing = False
                break

            player.stand = False


if __name__ == '__main__':
    main()
