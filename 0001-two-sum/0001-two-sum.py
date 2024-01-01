class Solution(object):
    def twoSum (self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target == nums[i] + nums[j]:
                    if i != j:
                        return [i,j]


sol = Solution()
result = sol.twoSum([2, 7, 11, 15], 9)
print(result)