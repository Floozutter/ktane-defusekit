"""
Functions for text autocompletion.
"""

from itertools import takewhile
from functools import reduce
from typing import Iterable, Optional


def common_prefix(a: str, b: str) -> str:
    """
    Returns the longest common prefix shared between two strings.
    """
    shared_chars = (pair[0] if pair[0] == pair[1] else None
                    for pair in zip(a, b))
    return "".join(takewhile(lambda char: char is not None, shared_chars))

def predict(wordbank: Iterable[str], initial: str) -> Optional[str]:
    """
    Returns a predictive suggestion from the initial string using the wordbank.
    If no words from the wordbank start with initial, None is returned.
    If only one word starts with initial, the full word is returned.
    If more than one word start with initial, the longest common prefix shared
    between the words is returned.
    """
    matches = [word for word in wordbank if word.startswith(initial)]
    if   len(matches) == 0:
        return None
    elif len(matches) == 1:
        return matches[0]
    else:
        return reduce(common_prefix, matches)
