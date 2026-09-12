class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left < right:

            capacity = (left + right) // 2

            current_weight = 0
            count_days = 1

            for weight in weights:

                if current_weight + weight > capacity:
                    count_days += 1
                    current_weight = 0

                current_weight += weight

            if count_days <= days:
                right = capacity
            else:
                left = capacity + 1

        return left