import pytest

from hangman import validate_input
from hangman import display_art
from hangman import check_win
from hangman import guess


def test_validate_input_number():
    with pytest.raises(TypeError):
        validate_input(1)


def test_validate_input_multiple():
    with pytest.raises(ValueError):
        validate_input("aa")


def test_validate_input_success():
    assert validate_input("a") is True


def test_display_art_lower():
    with pytest.raises(ValueError):
        display_art(-1)


def test_display_art_higher():
    assert display_art(8) == ValueError


def test_guess_single():
    assert guess(list("____"), "abcb", "a") == list("a___")


def test_guess_multiple():
    assert guess(list("____"), "abcb", "b") == list("_b_b")


def test_check_win_true():
    assert check_win("abc") is True


def test_check_false():
    assert check_win("_a_") is False
