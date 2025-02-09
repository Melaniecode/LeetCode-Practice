class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        for i in range(len(nums)):
            if target - nums[i] in numDict:
                return numDict[target - nums[i]], i
            numDict[nums[i]] = i # 將當前數字 nums[i] 作為鍵（key），並將其索引 i 作為值（value）存入字典 numDict

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]