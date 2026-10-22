class Solution:
    def countBits(self, n: int) -> List[int]:

        # O(nlogn) - time
        # O(n) - space (because of output size)

        # its possible to do this in O(n) using dp.

        ans = []
        for i in range(0, n+1):
            if i == 0:
                ans.append(0)
            else:
                curr = 0
                while True:
                    if i == 0:
                        break
                    elif i == 1:
                        curr += 1
                        break
                    print(i.bit_length() - 1)
                    print(i)
                    nearest_2_power = 1 << (i.bit_length() - 1)
                    curr += 1
                    i -= nearest_2_power
                ans.append(curr)
        
        return ans