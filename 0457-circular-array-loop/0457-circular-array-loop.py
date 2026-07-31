class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nextIndex(i, forward):
            direction = nums[i] >= 0

            if direction != forward:
                return -1

            next_i = (i + nums[i]) % n

            if next_i == i:
                return -1

            return next_i

        for i in range(n):
            forward = nums[i] > 0

            slow = i
            fast = i

            while True:
                slow = nextIndex(slow, forward)

                if slow == -1:
                    break

                fast = nextIndex(fast, forward)
                if fast == -1:
                    break

                fast = nextIndex(fast, forward)
                if fast == -1:
                    break

                if slow == fast:
                    return True

        return False