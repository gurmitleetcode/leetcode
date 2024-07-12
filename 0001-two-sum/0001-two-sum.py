class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if i != j:
                    output = nums[i] + nums[j]
                    if output == target:
                        return i, j
                j += 1
            i += 1
        return None  
nums = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums,target))