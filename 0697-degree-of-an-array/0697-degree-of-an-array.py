class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq ={}
        window ={}
        last = {}
        for i in range(len(nums)):
            num = nums[i]
            freq[num] = freq.get(num, 0) + 1

            if num not in window:
                window[num] =i
            last[num] =i    
        degree = max(freq.values())
        ans = len(nums)
        for num in freq:
            if freq[num] == degree:
                length = last[num] - window[num] +1
                ans = min(ans, length)
        return ans 
        

