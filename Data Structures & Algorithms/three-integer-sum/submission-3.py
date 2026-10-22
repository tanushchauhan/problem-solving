class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        s = {}
        for i, val in enumerate(nums):
            s[-val] = i
        ans = []
        ss = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                thing = nums[i] + nums[j]
                temp = tuple(sorted((nums[i], nums[j], -thing)))
                if thing in s and (s[thing] != i and s[thing] != j) and not(temp in ss):
                    ans.append([nums[i], nums[j], -thing])
                    ss.add(temp)
        
        return ans