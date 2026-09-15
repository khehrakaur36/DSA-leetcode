class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq={}
        window = {}
        for ch in s:
            freq[ch] = freq.get(ch , 0)+1
        for ch in t:
            if ch not in freq:
                return ch

            freq[ch]-=1
            if freq[ch]<0:
                return ch    