class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) time
        # O(n) - space
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False