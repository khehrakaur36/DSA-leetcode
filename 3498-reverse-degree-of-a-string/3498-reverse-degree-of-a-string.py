class Solution:
    def reverseDegree(self, s: str) -> int:
        res =0
        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))
            pos = i + 1
            res += value * pos
        return res    
