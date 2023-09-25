# Write a function `countConstruct(target, word_bank)` that accepts a
# target string and an array of strings.

# The function should return the number of ways that the `target` can
# be constructed by concatenating elements of the `word_bank` array.

# You may reuse elements of `word_bank` as many times as needed.

def count_construct(target, word_bank):
    tab = [0 for _ in range(len(target) + 1)]
    tab[0] = 1
    i = 0
    while i <= len(target):
        if tab[i] > 0:
            for word in word_bank:
                # if the word matches the character starting at position i
                if i + len(word) <= len(target) and target[i:].startswith(word):
                    tab[i + len(word)] = tab[i] + tab[i + len(word)]
        i += 1
    return tab[len(target)]


# m = len(target)
# n = len(word_bank)
# Time: O(m*n*m) -> (m^2 * n)
# Space: O(m)


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
