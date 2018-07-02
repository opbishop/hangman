import pytest

from hangman import validate_input
from hangman import display_art, HANGMANART


def test_validate_input_number():
    with pytest.raises(TypeError):
        validate_input(1)


def test_validate_input_multiple():
    with pytest.raises(ValueError):
        validate_input("aa")


def test_validate_input_success():
    assert validate_input("a") == True


def test_display_art_lower():
    with pytest.raises(ValueError):
        display_art(-1)


def test_display_art_higher():
    assert display_art(8) == ValueError
