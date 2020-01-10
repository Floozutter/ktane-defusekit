from functools import reduce
from itertools import takewhile


def common_prefix(a, b):
    shared_chars = (pair[0] if pair[0] == pair[1] else None
                    for pair in zip(a, b))
    return "".join(takewhile(lambda char: char is not None, shared_chars))

def predict(wordbank, ini):
    valids = [word for word in wordbank if word.startswith(ini)]
    if len(valids) == 0:
        return None
    elif len(valids) == 1:
        return valids[0]
    else:
        return reduce(common_prefix, valids)
