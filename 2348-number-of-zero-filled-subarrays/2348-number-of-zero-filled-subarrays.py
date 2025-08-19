class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        streak = 0
        result = 0
        for z in nums:
            if z == 0:
                streak += 1
                result += streak
            else:
                streak = 0
        return result
