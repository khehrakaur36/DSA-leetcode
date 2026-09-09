class Solution:
    def countCommas(self, n: int) -> int:
        ans =0
        comma_start = 1000
        while comma_start<=n:
            ans += n - comma_start +1
            comma_start *= 1000
        return ans 