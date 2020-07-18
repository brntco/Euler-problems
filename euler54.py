# from a provided txt file of one thousand poker games, determine the number of games the first player (of two) wins.

def number_check(hand):  # sort hand and discover hand type from card number only
    hand.sort(reverse=True)
    no_pairs = True
    pairvar = 0
    for item in hand:
        if hand.count(item) == 2:
            pairvar += (1 / 2)
            handrank = int(pairvar)  # either one or two pairs
            other_pair = False
            if other_pair == False:
                hand.pop(hand.index(item))
                hand.insert(0, item)
                other_pair = True  # keeps smaller pair from overwriting larger pair in decimal hand.
    for item in hand:
        if hand.count(item) == 3:  # check fullhouse and three of a kind
            hand.pop(hand.index(item))
            hand.insert(0, item)
            if pairvar == 1.0:
                handrank = 6
            else:
                handrank = 3
        if hand.count(item) == 4:  # check 4 of a kind
            hand.pop(hand.index(item))
            hand.insert(0, item)
            handrank = 7
        if hand.count(item) != 1:
            no_pairs = False
    if no_pairs == True:  # distinguish between straight and high card hands
        index = 0
        straight = True
        while index < len(hand) - 1:
            if hand[index] != hand[index + 1] + 1:
                straight = False
                break
            index += 1
        if straight == True:
            handrank = 4
        else:
            handrank = 0
    return handrank


def suit_check(suits, suited_rank):  # evaluate hand for suit related hand rank
    if len(set(suits)) == 1:  # check flush
        if suited_rank == 4:  # check straight flush
            suited_rank = 8  # no need to check royal flush, see decimal hand.
        else:
            suited_rank = 5
    return suited_rank


def decimal_hand(l):  # generate decimal number to ID card values in hand
    index = 0
    decihand = 0
    div = 100
    for each in l:
        decihand += (each / div)
        div *= 100
    return decihand


def handrank(hand):  # evaluate string list of cards in hand to a single, comparable value
    h_numstring = []
    h_num = []
    h_suit = []
    for card in hand:
        h_numstring.append(card[0])
        h_suit.append(card[1])
    for x in h_numstring:
        h_num.append(eval(x))
    rankvalue = suit_check(h_suit, number_check(h_num)) + decimal_hand(h_num)
    return rankvalue


def handify(l,n):  # create lists n items long from larger list
    for each in range(0, len(l), n):
        yield l[each:each+n]

f = open("poker.txt")
file = f.read()
games = file.replace("\n", " ")
game = list(handify(games.split(), 5))

T, J, Q, K, A = 10, 11, 12, 13, 14

p1 = list(game[0: len(game):2])
p2 = list(game[1: len(game):2])
p1wins = 0
for index in range(len(p1)):
    if handrank(p1[index]) > handrank(p2[index]):
        p1wins += 1

print(p1wins)
