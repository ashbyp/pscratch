from utils.measure import checker

class Solution:
    def maxProfit1(self, prices: list[int]) -> int:
        max_profit = 0
        for i, buy in enumerate(prices):
            for sell in prices[i+1:]:
                profit = sell - buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit

    def maxProfit2(self, prices: list[int]) -> int:
        max_profit = 0
        if prices:
            min_value = prices[0]
            for p in prices:
                if p < min_value:
                    min_value = p
                max_profit = max(max_profit, p - min_value)
        return max_profit


if __name__ == '__main__':
    with checker(Solution().maxProfit1, repeat=100000, check_success=True) as c:
        c.check_1([7,1,5,3,6,4], 5)
        c.check_1([7,6,4,3,1], 0)
    with checker(Solution().maxProfit2, repeat=100000, check_success=True) as c:
        c.check_1([7,1,5,3,6,4], 5)
        c.check_1([7,6,4,3,1], 0)

