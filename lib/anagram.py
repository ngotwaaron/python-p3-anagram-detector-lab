# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        for word in words:
            if sorted(word) == sorted(self.word) and word != self.word:
                anagrams.append(word)
        return anagrams