class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] != val:
                i += 1
                continue

            # Find a non-val element from the right.
            n -= 1
            while i < n and nums[n] == val:
                n -= 1

            if i < n:
                nums[i] = nums[n]
                i += 1

        return n