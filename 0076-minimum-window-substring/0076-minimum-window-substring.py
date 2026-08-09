class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq1 = {}
        freq2 = {}

        for ch in t:
            freq1[ch] = freq1.get(ch, 0) + 1

        left = 0
        ans = ""

        for right in range(len(s)):
            freq2[s[right]] = freq2.get(s[right], 0) + 1

            while right - left + 1 >= len(t):

                valid = True

                for ch in freq1:
                    if ch not in freq2 or freq2[ch] < freq1[ch]:
                        valid = False
                        break

                if valid == False:
                    break

                curr = s[left:right + 1]

                if ans == "" or len(curr) < len(ans):
                    ans = curr

                freq2[s[left]] -= 1

                if freq2[s[left]] == 0:
                    del freq2[s[left]]

                left += 1

        return ans