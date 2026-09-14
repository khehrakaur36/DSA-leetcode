class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq ={}
        n= len(nums)
        for num in nums:
            freq[num] = freq.get(num ,0)+1
        duplicate = 0
        missing = 0
        for num in range(1, n+1):
            if num in freq:
                if freq[num]>1:
                   duplicate = num
            if num not in freq:
                missing = num
        return [duplicate , missing]            


