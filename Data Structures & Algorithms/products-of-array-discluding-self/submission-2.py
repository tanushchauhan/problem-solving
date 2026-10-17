class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #target
        # O(n) - time 
        # O(n) - space


        prefix = []
        suff = []
        curr = 1
        for i in nums:
            curr *= i
            prefix.append(curr)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            curr *= nums[i]
            suff.append(curr)
        suff.reverse()
        ans = []
        for i in range(len(nums)):
            if (i == 0):
                ans.append(suff[i + 1])
            elif (i == len(nums) - 1):
                ans.append(prefix[len(nums) - 2])
            else:
                ans.append(prefix[i - 1] * suff[i+1])
        return ans