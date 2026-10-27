class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 256
        for char in s:
            freq[ord(char)] += 1
        for char in t:
            freq[ord(char)] -= 1
        return all(count == 0 for count in freq)