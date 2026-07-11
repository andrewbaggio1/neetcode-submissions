class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = current = 0
        for num in nums:
            if num:
                current += 1
                if current > longest:
                    longest = current
            else:
                current = 0
        return longest
        