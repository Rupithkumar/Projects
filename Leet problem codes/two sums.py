class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) <= 0:
            print('false')

        dict1 = {}
        for t in range(len(nums)):
            if nums[t] in dict1:
                return [dict1[nums[t]], t]
            else:
                dict1[target - nums[t]] = t