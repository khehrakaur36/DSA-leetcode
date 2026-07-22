class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt ={}
        for i, num in enumerate(nums):
            needed = target - nums[i]
            if needed in dictt:
                return [dictt[needed], i]
            dictt[num]=i
