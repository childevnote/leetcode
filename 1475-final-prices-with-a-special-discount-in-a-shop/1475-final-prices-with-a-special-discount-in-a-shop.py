class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            is_appended = False
            for j in range(i+1, len(prices)):
                if prices[i]>=prices[j] :
                    res.append(prices[i]-prices[j])
                    is_appended = True
                    break 
            if is_appended == False :
                res.append(prices[i])
        return res