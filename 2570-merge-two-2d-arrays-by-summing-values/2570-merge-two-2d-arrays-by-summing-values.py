class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        values = {}

        for id, value in nums1:
            values[id] = values.get(id, 0) + value

        for id, value in nums2:
            values[id] = values.get(id, 0) + value

        ans = []

        for id in sorted(values):
            ans.append([id, values[id]])

        return ans