class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) - time
        # O(n) - space
        buckets = [[] for _ in range(len(nums) + 1)]
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for key, val in dic.items():
            buckets[val].append(key)
        c = k
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for w in buckets[i]:
                ans.append(w)
                c -= 1
                if c == 0:
                    return ans