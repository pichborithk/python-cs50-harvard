# Simple Blackjack Project

##### Video Demo: https://youtu.be/0o34AX2SoEE

### Description:

This is an application that allow player to plays a simple Blackjack game with computer.

### Getting Start

Fork and clone this repo to your local machine, then run the following commands:

`python project.py` or `python3 project.py`

### How application works:

1. After start the application, the program will render the Blackjack logo to display on the terminal screen.

```python
  print(logo)
```

2. A new set of deck will create by Deck class which we can freely set it to generate a full set of deck or more, or only 13 cards with random suit.

```python
  deck = Deck.create(full_set=False)
```

```python
  class Deck:
      ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
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
```

3. Player and Computer got random 2 cards from deck with `deal_card` function, which using Card class to initialize properties for card.

```python
  player_hand = [deal_card(deck), deal_card(deck)]
  computer_hand = [deal_card(deck), deal_card(deck)]
```

```python
  def deal_card(deck):
    card_in_deck = random.choice(deck)
    deck.remove(card_in_deck)
    return Card(*card_in_deck)
```

```python
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
```

4. Calculate the score for both Player and Computer using `calculate_hand` function.

```python
  player_score = calculate_hand(player_hand)
  computer_score = calculate_hand(computer_hand)
```

```python
  def calculate_hand(hand):
    cards = [card.get_value() for card in hand]

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
```

5. Display Player's hand and Computer's hand on terminal screen using `display_cards` function, but 1 of the Computer's cards got hidden.

```python
  print("Computer Hand")
  display_cards(computer_hand, hidden=True)
  print("Your Hand")
  display_cards(player_hand)
```

```python
  def display_cards(hand, hidden=False):
    cards = []
    for i, card in enumerate(hand):
        if hidden and i == 0:
            cards.append(card.render_card(hidden=True))
        else:
            cards.append(card.render_card())

    for i in range(7):
        for card in cards:
            print(card[i], end="")

        print("")
```

6. Check score on both hands using `is_game_over` function if any of hand got Blackjack break from `while loop` to end the game.

```python
  if is_game_over(player_score, computer_score):
            break
```

```python
  def is_game_over(player_score, computer_score):
    if player_score == 0 or computer_score == 0 or player_score > 21:
        return True
    else:
        return False
```

7. Otherwise, the program will continue prompt to ask Player if they want to draw another card until Player hand went over 21 or choose not to draw.

```python
   if is_game_over(player_score, computer_score):
            break
        else:
            player_should_deal = (
                input("Type 'YES' to get another card, type 'NO' to pass: ")
                .strip()
                .lower()
            )
            if player_should_deal[0] == "y":
                player_hand.append(deal_card(deck))
            else:
                break
```

8. After Player passed on draw more card or their hand went over 21, Computer will continue to draw card if its hand is less than 17 until its hand greater or equal to 17.

```python
   while computer_score < 17 and computer_score != 0 and player_score != 0:
        computer_hand.append(deal_card(deck))
        computer_score = calculate_hand(computer_hand)
```

9. Finally, the program will compare both hand using `compare` function and display who the winner is.

```python
  print("Computer Hand")
  display_cards(computer_hand)
  print("Your Hand")
  display_cards(player_hand)
  print(compare(player_score, computer_score))
```

```python
  def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif player_score == 0:
        return "Win with a Blackjack"
    elif player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose"
```
