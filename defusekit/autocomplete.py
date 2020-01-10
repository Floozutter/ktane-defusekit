from functools import reduce


def shared_start(a, b):
    indices_of_diff = (i for i, pair in enumerate(zip(a, b))
                       if pair[0] != pair[1])
    size = next(indices_of_diff, min(len(a), len(b)))
    return a[:size]

def predict(wordbank, ini):
    valids = [word for word in wordbank if word.startswith(ini)]
    if len(valids) == 0:
        return None
    elif len(valids) == 1:
        return valids[0]
    else:
        return reduce(shared_start, valids)
