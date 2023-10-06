from project import calculate_hand, is_game_over, compare
from card import Card


def test_game_over():
    assert is_game_over(player_score=0, computer_score=14)
    assert is_game_over(player_score=20, computer_score=0)
    assert is_game_over(player_score=24, computer_score=12)
    assert not is_game_over(player_score=10, computer_score=15)


def test_calculate_hand():
    assert calculate_hand([Card("2", "♥"), Card("5", "♦")]) == 7
    assert calculate_hand([Card("Ace", "♣"), Card("King", "♥")]) == 0
    assert calculate_hand([Card("Ace", "♦"), Card("7", "♠"), Card("3", "♥")]) == 21
    assert calculate_hand([Card("Ace", "♠"), Card("Ace", "♥"), Card("9", "♠")]) == 21
    assert calculate_hand([Card("King", "♥"), Card("Jack", "♥"), Card("9", "♣")]) == 29


def test_compare():
    assert compare(player_score=19, computer_score=19) == "Draw"
    assert compare(player_score=0, computer_score=17) == "Win with a Blackjack"
    assert compare(player_score=12, computer_score=0) == "Lose, opponent has Blackjack"
    assert compare(player_score=23, computer_score=18) == "You went over. You lose"
    assert compare(player_score=20, computer_score=25) == "Opponent went over. You win"
    assert compare(player_score=20, computer_score=19) == "You win"
    assert compare(player_score=18, computer_score=20) == "You lose"

