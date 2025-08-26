class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plot = 0
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 1:
            return False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            plot += 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 :
                flowerbed[i] = 1
                plot += 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            plot += 1
        return True if plot >= n else False
            

        

        