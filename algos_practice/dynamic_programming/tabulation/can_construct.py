# Write a function `can_construct(target, word_bank)` that accepts a
# target string and an array of strings.

# The function should return a boolean indicating whether or not the
# `target` can be constructed by concatenating elements of the
# `word_bank array.

# You may reuse elements of word_bank as many times as needed.

def can_construct(target, word_bank):
    tab = [False for _ in range(len(target) + 1)]
    tab[0] = True
    i = 0
    while i <= len(target):
        if tab[i] == True:
            for word in word_bank:
                # if the word matches the character starting at position i
                if i + len(word) <= len(target) and target[i:].startswith(word):
                    tab[i + len(word)] = True
        i += 1
    return tab[len(target)]

# m = len(target)
# n = len(word_bank)
# Time: O(m*n*m) -> (m^2 * n)
# Space: O(m)

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
