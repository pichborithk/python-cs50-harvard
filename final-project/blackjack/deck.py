import random


class Deck:
    ranks = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    suits = ["♥", "♣", "♦", "♠"]

    @staticmethod
    def create(full_set=True, deck_set=1):
        deck = []
        if not full_set:
            suit = random.choice(Deck.suits)
            for rank in Deck.ranks:
                deck.append((rank, suit))
        else:
            for _ in range(deck_set):
                for suit in Deck.suits:
                    for rank in Deck.ranks:
                        deck.append((rank, suit))

        return deck
