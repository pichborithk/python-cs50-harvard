from art import card_art, hidden_card_art


class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def icon(self):
        match self._rank:
            case "Ace" | "King" | "Queen" | "Jack":
                return self._rank[0]
            case _:
                return self._rank

    def get_value(self):
        match self._rank:
            case "Ace":
                return 11
            case "King" | "Queen" | "Jack":
                return 10
            case _:
                return int(self._rank)

    def render_card(self, hidden=False):
        if hidden:
            return hidden_card_art
        else:
            card = [*card_art]
            card[3] = card[3].format(self.suit)
            if self._rank == "10":
                card[1] = card[1].format(self.icon, "")
                card[5] = card[5].format("", self.icon)
            else:
                card[1] = card[1].format(self.icon, " ")
                card[5] = card[5].format(" ", self.icon)

            return card
