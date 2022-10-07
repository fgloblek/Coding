from string import ascii_letters


class trie_node:
    """Trie, each node has 52 kids, most empty."""

    def __init__(self):
        self.is_word = False
        self.s = {c: None for c in ascii_letters}


def add(T, w, i=0):
    if T is None:
        T = trie_node()
    if i == len(w):
        T.is_word = True
    else:
        T.s[w[i]] = add(T.s[w[i]], w, i + 1)
    return T


def trie(S):
    T = None
    for w in S:
        add(T, w)
    return T
