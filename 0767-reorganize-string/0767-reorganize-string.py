import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap=[]
        res =""
        freq ={}
        for ch in range(len(s)):
            freq[s[ch]] = freq.get(s[ch],0)+1
        for ch , count in freq.items():
            if count > (len(s)+1)//2:
                return ""
            heapq.heappush(heap, (-count, ch))
        prev_count =0
        prev_char =""    
        while heap:
            count , ch = heapq.heappop(heap)
            res+=ch
            count +=1

            
            if prev_count< 0:
                heapq.heappush(heap, (prev_count, prev_char))
            prev_char = ch
            prev_count = count    
        return res    
                
