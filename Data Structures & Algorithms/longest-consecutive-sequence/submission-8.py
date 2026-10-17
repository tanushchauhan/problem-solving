class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = {}
        maxt = 1
        for v in nums:
            s[v] = None
        for i, _ in s.items():
            if i - 1 in s:
                continue
            m = 1
            x = i
            while(x+1 in s):
                if (s[x+1] != None):
                    m += s[x+1]
                    break
                m += 1
                x += 1
            maxt = max(maxt, m)
            s[i] = m
        
        return maxt
