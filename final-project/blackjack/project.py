import random
from card import Card
from deck import Deck
from art import logo


def main():
    print(logo)
    deck = Deck.create(full_set=False)

    player_hand = [deal_card(deck), deal_card(deck)]
    computer_hand = [deal_card(deck), deal_card(deck)]

    while True:
        player_score = calculate_hand(player_hand)
        computer_score = calculate_hand(computer_hand)
        print("Computer Hand")
        display_cards(computer_hand, hidden=True)
        print("Your Hand")
        display_cards(player_hand)


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

    while computer_score < 17 and computer_score != 0 and player_score != 0:
        computer_hand.append(deal_card(deck))
        computer_score = calculate_hand(computer_hand)

    print("Computer Hand")
    display_cards(computer_hand)
    print("Your Hand")
    display_cards(player_hand)
    print(compare(player_score, computer_score))


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


def is_game_over(player_score, computer_score):
    if player_score == 0 or computer_score == 0 or player_score > 21:
        return True
    else:
        return False


def calculate_hand(hand):
    cards = [card.get_value() for card in hand]

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def deal_card(deck):
    card_in_deck = random.choice(deck)
    deck.remove(card_in_deck)
    return Card(*card_in_deck)


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


if __name__ == "__main__":
    main()
