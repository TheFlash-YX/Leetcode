class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        # 初始状态：买入股票需要花钱，所以初始化为负无穷大（极小值）
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for price in prices:
            # 状态转移顺序可以并列，因为取的是最大值，"幽灵交易"会自我抵消
            buy1 = max(buy1, -price)  # 第 1 次买入后手里的钱
            sell1 = max(sell1, buy1 + price)  # 第 1 次卖出后手里的钱
            buy2 = max(buy2, sell1 - price)  # 第 2 次买入后手里的钱
            sell2 = max(sell2, buy2 + price)  # 第 2 次卖出后手里的钱

        # 最终肯定是把股票卖掉赚的钱最多，返回 sell2
        return sell2