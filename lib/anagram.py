class Anagram:
    def __init__(self, new_anagram):
        self.new_anagram = new_anagram

    def match(self, possible_anagrams):
        return [word for word in possible_anagrams if sorted(word) == sorted(self.new_anagram)]