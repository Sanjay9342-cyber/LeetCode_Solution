class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        if len(word) != len(pattern):
            return False
        return len(set(word))==len(set(pattern))==len(set(zip(word,pattern)))