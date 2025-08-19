class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        arr = []
        streakFlag = False
        streak = 0
        result = 0
        for z in nums:
            if z == 0:
                streak += 1
                streakFlag = True
            if z != 0 and streakFlag == True:
                arr.append(streak)
                streak = 0
                streakFlag = False

        if streak:
            arr.append(streak)

        for a in arr:
            result += a*(a+1)//2

        return result