class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n - length og strs
        # m - len of the longest string in strs
        # O(n * m) - time complexity
        # O(m) - space complexity
        ans = []
        dic = {}
        curr = None
        for i in strs:
            curr = [0] * 26
            for g in i:
                curr[ord(g) - ord('a')] += 1
            curr = tuple(curr)
            if curr in dic:
                dic[curr].append(i)
            else:
                dic[curr] = [i]

        for i, j in dic.items():
            ans.append(j)

        return ans