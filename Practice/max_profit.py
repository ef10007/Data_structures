class MaxProfit(object):
    def single_transaction(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = prices[1:]
        first_day = sell[0]
        if max(sell) > first_day:
            return max(sell) - first_day
        else:
            return 0

    def multiple_transaction(self, prices):
        profit = 0
        i = 1
        while i < len(prices):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            i += 1
        return profit

print(MaxProfit().multiple_transaction([2,4,1]))