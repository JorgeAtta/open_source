# -*- coding: utf-8 -*-
"""Main module."""

# Standard library imports
import random
import string


def check_palindrome(word):
    """Check if a word is a palindrome."""
    reverse = word[::-1]
    word = word.upper()
    reverse = reverse.upper()
    
    if (word == reverse):
        return True
    else:
        return False

    



def random_letter(word=None):
    """Return a random letter of the alphabet."""
    if word:
        letters = word
    else:
        letters = string.ascii_letters

    index = random.randint(0, len(letters))
    return letters[index]


def random_int(lower, upper):
    """Return a random integer from the alphabet."""
    return random.randint(lower, upper)
