import random

SUITE = 'S D C H'.split()
RANK = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
rank_value = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
              '9':9, '10':10,'J':10, 'Q':10, 'K':10}


class Deck():
    def __init__(self):
        self.allcards = [(s,r) for s in SUITE for r in RANK]

    def remove_from_deck(self):
        self.allcards.pop(0)


class Hand():
    def __init__(self,cards):
        self.cards = cards

    def add_to_hand(self, added_cards):
        self.cards.append(added_cards)

    def find_score(self):
        for x in self.cards[::-1]:
            rank = x[1]
            return rank_value[rank]


class Player():
    def __init__(self,name,Hand):
        self.name = name
        self.Hand = Hand



## INTRO ##
deck = []
deck_cards = Deck()
deck.extend(deck_cards.allcards)
print("New deck created")
random.shuffle(deck)

# Creating the Players
dealer = Player('Dealer', Hand([]))
name = input("What is your name? ")
player = Player(name, Hand([]))


## GAMEPLAY ##
player_score = 0
dealer_score = 0

n = 1
while n<3:
    card = deck.pop()
    player.Hand.add_to_hand(card)
    player_card_score = player.Hand.find_score()
    player_score += player_card_score
    if player_score == 21:
        print(name + " has 21 and has won the game!")
        break
    n = n + 1

if player_score != 21:
    n = 1
    while n<3:
        card = deck.pop()
        dealer.Hand.add_to_hand(card)
        dealer_card_score = dealer.Hand.find_score()
        dealer_score += dealer_card_score
        if dealer_score == 21:
            print("Dealer has 21 and has won the game!")
            break
        n = n + 1

if player_score and dealer_score != 21:
    new_p_score = 0
    new_d_score = 0
    n = 1
    while n <= 17:
        card = deck.pop()
        player.Hand.add_to_hand(card)
        new_player_card_score = player.Hand.find_score()
        new_p_score += new_player_card_score
        if new_p_score == 21:
            print(name + " has 21 and has won the game!")
            break
        else:
            if new_p_score > 21:
                print(name + " has a total higher than 21 and has lost the game")
                break

        n = n + 1

    if new_p_score != 21:
        while new_d_score < new_p_score:
            card = deck.pop()
            dealer.Hand.add_to_hand(card)
            new_dealer_card_score = dealer.Hand.find_score()
            new_d_score += new_dealer_card_score
            if new_d_score == 21:
                print("Dealer has 21 and has won the game!")
                break
            else:
                if new_d_score > 21:
                    print("Dealer has a total higher than 21 and has also lost the game")
                    print("Neither player has won")
                    break
