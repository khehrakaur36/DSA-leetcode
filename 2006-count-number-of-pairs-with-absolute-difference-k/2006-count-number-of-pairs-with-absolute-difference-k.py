class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = {}
        ans = 0
        for num in nums:
            if num + k in freq:
                ans += freq[num + k]

            if num - k in freq:
                ans += freq[num - k]

            freq[num] = freq.get(num, 0) + 1

        return ans