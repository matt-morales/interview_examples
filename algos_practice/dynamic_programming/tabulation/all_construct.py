# Write a function `all_construct(target, word_bank)` that accepts a
# taget string and an array of strings.

# The function should return a 2D array containing all of the ways
# that the `target` can be constructed by concatenating elements  of
# the `word_bank` array. Each element of the 2D array should represeent
# one combination that constructs the `target`.

# You may reuse elements of `word_bank` as many times as needed.


def all_construct(target, word_bank):
    tab = [[] for _ in range(len(target) + 1)]
    tab[0] = [[]]
    i = 0
    while i <= len(target):
        if len(tab[i]) > 0:
            for word in word_bank:
                # if the word matches the character starting at position i
                if target[i:].startswith(word):
                    new_combos = [
                        [*combo, word]
                        for combo in tab[i]
                    ]
                    tab[i + len(word)].extend(new_combos)
        i += 1
    return tab[len(target)]

from pprint import pprint

pprint(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
pprint(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
pprint(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
pprint(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
pprint(all_construct("eeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
