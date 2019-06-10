"""OOP Project"""
from random import shuffle
SUITE = ['H', 'D', 'S', 'C']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Deck:
    """This is the Deck Class."""
    def __init__(self):
        print("Creating New Ordered Deck!")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        """Shuffling Deck"""
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        """
        :return: (2nd half, 1st half)
        """
        return self.allcards[:26], self.allcards[26:]


class Hand:
    """This is the Hand class"""
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        """
        :param added_cards: Add cards to hand
        """
        self.cards.extend(added_cards)

    def remove_card(self):
        """
        :return: return the 1 card being removed from hand
        """
        return self.cards.pop()


class Player:
    """This is the Player class"""
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        """
        :return: the card that is being drawn
        """
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card), "\n")
        return drawn_card

    def remove_war_cards(self):
        """
        :return: removed card
        """
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for _ in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """Return True if player still has cards left"""
        return len(self.hand.cards) != 0


print("Welcome to War, let's begin...")
# Create new deck and split it in half
D = Deck()
D.shuffle()
HALF1, HALF2 = D.split_in_half()
# Create both players!
COMP = Player("computer", Hand(HALF1))
NAME = input("What is your name: ")
USER = Player(NAME, Hand(HALF2))
TOTAL_ROUNDS = 0
WAR_COUNT = 0

while USER.still_has_cards() and COMP.still_has_cards():
    TOTAL_ROUNDS += 1
    print("Time for a new round!")
    print("Here are the current standings.")
    print(USER.name + " had the count: " + str(len(USER.hand.cards)))
    print(COMP.name + " had the count: " + str(len(COMP.hand.cards)))
    print("Play a card!\n")
    TABLE_CARDS = []
    C_CARD = COMP.play_card()
    P_CARD = USER.play_card()
    TABLE_CARDS.append(C_CARD)
    TABLE_CARDS.append(P_CARD)

    if C_CARD[1] == P_CARD[1]:
        WAR_COUNT += 1
        print("WAR!")
        TABLE_CARDS.extend(USER.remove_war_cards())
        TABLE_CARDS.extend(COMP.remove_war_cards())
        if RANKS.index(C_CARD[1]) < RANKS.index(P_CARD[1]):
            USER.hand.add(TABLE_CARDS)
        else:
            COMP.hand.add(TABLE_CARDS)
    else:
        if RANKS.index(C_CARD[1]) < RANKS.index(P_CARD[1]):
            USER.hand.add(TABLE_CARDS)
        else:
            COMP.hand.add(TABLE_CARDS)

print("Game Over, number of rounds: " + str(TOTAL_ROUNDS))
print("A war happened " + str(WAR_COUNT) + " times.")
print("Does the computer still have cards? ")
print(str(COMP.still_has_cards()))
print("Does the human players still have cards? ")
print(str(USER.still_has_cards()))
