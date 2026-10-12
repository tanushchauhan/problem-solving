class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # o(n) - time
        # o(n) - space
        dic = {}
        for i in range(len(nums)):
            c = nums[i]
            a = target - c
            if a in dic:
                return [dic[a], i]
            dic[c] = i
        
        return []