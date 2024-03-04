# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w)]

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return sorted(self.word) == sorted(candidate_lower) and self.word != candidate_lower
