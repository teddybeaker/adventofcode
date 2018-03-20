def is_valid_passphrase(passphrase):
    words = passphrase.split(" ")
    for word in words:
        if words.count(word) > 1:
            return False
    return True

def is_valid_passphrase_strict(passphrase):
    words = passphrase.split(" ")
    for i in range(0, len(words)):
        for j in range(i, len(words)):
            if (i != j):
                if is_anagram(words[i], words[j]):
                    return False
    return True

def is_valid_passphrase_strict2(passphrase):
    words = passphrase.split(" ")
    sorted_words = ["".join(sorted(w)) for w in words]
    for word in sorted_words:
        if sorted_words.count(word) > 1:
            return False
    return True

def is_anagram(word1, word2):
    if word1 == word2:
        return True
    if len(word1) != len(word2):
        return False
    for char in word1:
        if word1.count(char) != word2.count(char):
            return False
    return True



if __name__ == "__main__":
    sum1 = sum2 = sum3 = 0
    count = 0
    with open("./input.txt") as f:
        content = f.read()
        for line in content.split("\n"):
            count += 1
            passphrase = line.strip()
            if len(passphrase):
                if is_valid_passphrase(passphrase):
                    sum1 += 1
                if is_valid_passphrase_strict(passphrase):
                    sum2 += 1
                if is_valid_passphrase_strict2(passphrase):
                    sum3 += 1
    f.closed

    if sum2 != sum3:
        raise Exception("did get different number of valid passphrases with different methods: %d, %d" % (sum2, sum3))

    print("found %d valid passphrases with unique words in %d" % (sum1, count))
    print("found %d valid passphrases without anagrams in %d" % (sum2, count))
