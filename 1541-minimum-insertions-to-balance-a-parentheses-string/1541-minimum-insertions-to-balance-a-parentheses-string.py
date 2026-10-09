class Solution:
    def minInsertions(self, s: str) -> int:
        open = 0
        add = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1

            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    add += 1

                if open > 0:
                    open -= 1
                else:
                    add += 1

            i += 1

        return add + 2 * open