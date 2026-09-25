class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        MOD = 10**9 + 7
        freq = {}
        ans = 0

        powers = []

        for i in range(22):
            powers.append(2 ** i)

        for num in deliciousness:
            for power in powers:
                need = power - num

                if need in freq:
                    ans += freq[need]

            freq[num] = freq.get(num, 0) + 1

        return ans % MOD