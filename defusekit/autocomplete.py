"""
Functions for text autocompletion.
"""

from itertools import takewhile
from functools import reduce
from typing import Optional, Iterable


def common_prefix(a: str, b: str) -> str:
    """
    Returns the longest common prefix shared between two strings.
    """
    shared_chars = (l if l == r else "" for l, r in zip(a, b))
    return "".join(takewhile(lambda char: bool(char), shared_chars))

def predict(wordbank: Iterable[str], initial: str) -> Optional[str]:
    """
    Returns a continuation of the initial string using the wordbank.
    If no words from the wordbank start with initial, None is returned.
    If only one word starts with initial, the full word is returned.
    If more than one word start with initial, the longest common prefix shared
    between the words is returned.
    """
    matches = list(filter(lambda word: word.startswith(initial), wordbank))
    if   len(matches) == 0: return None
    elif len(matches) == 1: return matches[0]
    else:                   return reduce(common_prefix, matches)
