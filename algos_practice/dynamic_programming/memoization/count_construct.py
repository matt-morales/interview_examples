# Write a function `countConstruct(target, word_bank)` that accepts a
# target string and an array of strings.

# The function should return the number of ways that the `target` can
# be constructed by concatenating elements of the `word_bank` array.

# You may reuse elements of `word_bank` as many times as needed.

def count_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            num_ways = count_construct(target[len(word):], word_bank)
            total_count += num_ways

    memo[target] = total_count
    return total_count

print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"], {}))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], {}))
