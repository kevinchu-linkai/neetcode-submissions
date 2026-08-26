class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = {}
        for i in range(len(nums)):
            m = target - nums[i]
            if m in k:
                return [k[m], i]
            k[nums[i]] = i