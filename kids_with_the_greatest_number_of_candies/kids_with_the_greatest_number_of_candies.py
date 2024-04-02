class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_num = max(candies)
        for i in candies:
            real = i + extraCandies
            result.append(real >= max_num)
        return result
