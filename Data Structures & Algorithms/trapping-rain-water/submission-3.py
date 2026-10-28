class Solution:
    def trap(self, height: List[int]) -> int:
        fu = []
        m = 0
        for i in range(len(height) - 1, -1, -1):
            fu.append(m)
            m = max(m, height[i])
        fu.reverse()
        lu = []
        m = 0
        for i in range(0, len(height)):
            lu.append(m)
            m = max(m, height[i])
        ans = 0
        for i in range(1, len(height) - 1):
            some = min(lu[i], fu[i])
            if(height[i] < some):
                ans += some - height[i]
        
        return ans
