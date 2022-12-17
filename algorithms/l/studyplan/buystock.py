from typing import List
from utils.measure import checker


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]
        for p in prices:
            if p < min_price:
                min_price = p
            if p - min_price > max_profit:
                max_profit = p - min_price

        return max_profit


if __name__ == '__main__':
    with checker(Solution().maxProfit, repeat=1000, check_success=True) as c:
        c.check_1([7,1,5,3,6,4], 5)
        c.check_1([7,6,4,3,1], 0)
