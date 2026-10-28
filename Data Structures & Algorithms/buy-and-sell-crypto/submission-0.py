class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fu = []
        m = 0
        for i in range(len(prices) - 1, -1, -1):
            fu.append(m)
            m = max(m, prices[i])
        fu.reverse()
        m_profit = 0
        for i in range(0, len(prices)):
            m_profit = max(m_profit, fu[i] - prices[i])
        return m_profit