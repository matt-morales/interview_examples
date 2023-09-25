# Write a function `can_construct(target, word_bank)` that accepts a
# target string and an array of strings.

# The function should return a boolean indicating whether or not the
# `target` can be constructed by concatenating elements of the
# `word_bank array.

# You may reuse elements of word_bank as many times as needed.

def can_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            idx = len(word)
            suffix = target[idx:]
            if can_construct(suffix, word_bank, memo) == True:
                memo[target] = True
                return True

    memo[target] = False
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], {}))
