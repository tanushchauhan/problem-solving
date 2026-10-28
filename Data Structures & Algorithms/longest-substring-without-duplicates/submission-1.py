class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        ar = [0] * 256
        l = 0
        r = 0
        ar[ord(s[l])] += 1
        m = 0
        while(r < len(s) and l < len(s)):
            while r < len(s)-1:
                r += 1
                if (ar[ord(s[r])] == 0):
                    ar[ord(s[r])] += 1
                else:
                    r -= 1
                    break
            m = max(m, (r - l + 1))
            ar[ord(s[l])] -= 1
            l += 1
        
        return m