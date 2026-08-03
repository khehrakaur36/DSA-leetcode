class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def fun(candidates, n, idx, diary, res, summ):
            if idx == n:
                if summ == target:
                    res.append(diary[:])
                return

            # Skip current element
            fun(candidates, n, idx + 1, diary, res, summ)

            # Take current element
            if summ + candidates[idx] <= target:
                diary.append(candidates[idx])
                fun(candidates, n, idx, diary, res, summ + candidates[idx])
                diary.pop()

        res = []
        fun(candidates, len(candidates), 0, [], res, 0)
        return res