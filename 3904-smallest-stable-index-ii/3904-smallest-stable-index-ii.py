class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0]*n
        suffix_min[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i+1])

        largest = nums[0]
        for i in range(n):
            largest = max(largest, nums[i])

            if largest - suffix_min[i] <= k:
                return i 
        return -1            