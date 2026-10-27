class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n=len(citations)
        citations.sort()
        for i, c in enumerate(citations):
            if n-i <= c:
                return n-i
        return 0