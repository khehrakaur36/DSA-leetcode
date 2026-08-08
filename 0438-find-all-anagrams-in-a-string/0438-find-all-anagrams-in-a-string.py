class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq ={}
        window ={}
        for ch in range(len(p)):
            freq[p[ch]] = freq.get(p[ch], 0)+1
        
        left =0
        ans =[]
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0)+1
         
        
            if right-left+1 ==len(p):
                if window == freq:
                  ans.append(left)
                window[s[left]] -=1
            
                if window[s[left]]==0:
                    del window[s[left]] 
                left+=1
        return ans        