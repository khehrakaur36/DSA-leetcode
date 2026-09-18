class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        first = {}
        last = {}

        # Find first and last position
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        candidates = []

        # Try every character
        for ch in first:

            start = first[ch]
            end = last[ch]
            i = start
            valid = True

            while i <= end:
                current = s[i]

                # This character occurs before our start
                if first[current] < start:
                    valid = False
                    break

                # Need to include all occurrences
                end = max(end, last[current])

                i += 1

            if valid:
                candidates.append((start, end))

        # Choose non-overlapping intervals
        candidates.sort(key=lambda x: x[1])

        answer = []
        end = -1

        for start, finish in candidates:
            if start > end:
                answer.append(s[start:finish + 1])
                end = finish

        return answer