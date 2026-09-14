class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq ={}
        nums.sort()
        for num in nums:
            freq[num] = freq.get(num,0)+1
        low = 0
        high = len(nums)-1
        
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == mid:
                low = mid +1
            else:
                high = mid-1    
        return low