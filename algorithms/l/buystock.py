# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.


class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i, buy in enumerate(prices):
            for sell in prices[i+1:]:
                profit = sell - buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit


def main():
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([7,6,4,3,1]))


if __name__ == '__main__':
    main()