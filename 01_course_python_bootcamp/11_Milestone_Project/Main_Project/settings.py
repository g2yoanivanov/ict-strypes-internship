DECKS_NUMBER = 6
CARDS_IN_DECK = 52

TOTAL_CARDS = DECKS_NUMBER * CARDS_IN_DECK
SHUFFLE_PERCENT = 0.25

CASINO_FUNDS = 2000000

BJ_COEFF = 3/2

suits = (
    '♣',
    '♦',
    '♥',
    '♠',
)

ranks = (
    '2', '3', '4', '5',
    '6', '7', '8', '9',
    '10', 'J', 'Q', 'K', 'A'
)

values = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10,
    'K': 10, 'A': (1, 11)
}