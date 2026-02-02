class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find two numbers that add up to target using hash table."""
        seen = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i
        return []
