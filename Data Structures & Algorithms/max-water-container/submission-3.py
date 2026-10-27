class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(N) - time
        # O(1) - space
        l = 0
        r = len(heights) - 1
        ans = 0
        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            ans = max(ans, curr)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return ans