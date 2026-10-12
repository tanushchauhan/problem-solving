class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #target
        # o(n) - time
        # o(n) - space

        if len(s) != len(t):
            return False
        a1 = {}
        for i in range(len(s)):
            if s[i] in a1:
                a1[s[i]] += 1
            else:
                a1[s[i]] = 1
        for i in range(len(s)):
            if t[i] in a1:
                a1[t[i]] -= 1
                if a1[t[i]] == 0:
                    del a1[t[i]];
            else:
                return False

        return a1 == {}