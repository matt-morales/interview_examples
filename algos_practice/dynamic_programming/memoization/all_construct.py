# Write a function `all_construct(target, word_bank)` that accepts a
# taget string and an array of strings.

# The function should return a 2D array containing all of the ways
# that the `target` can be constructed by concatenating elements  of
# the `word_bank` array. Each element of the 2D array should represeent
# one combination that constructs the `target`.

# You may reuse elements of `word_bank` as many times as needed.

def all_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    res = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = [
                [word, *way]
                for way in suffix_ways
            ]
            res += target_ways

    memo[target] = res
    return res

from pprint import pprint

pprint(all_construct("purple", ["purp", "p", "ur", "le", "purpl"], {}))
pprint(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], {}))
pprint(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
pprint(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))
pprint(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], {}))
