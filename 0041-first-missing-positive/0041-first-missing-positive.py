class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        freq ={}
        ans =[]
        for num in nums:
            freq[num] = freq.get(num ,0)+1
        for num in range(1 , len(nums)+2):
            if num not in freq:
                return num