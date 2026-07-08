class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            desiredNumber = target - nums[i]
            
            if desiredNumber in nums and nums.index(desiredNumber) != i:
                if i > nums.index(desiredNumber):
                    return [nums.index(desiredNumber), i]
                return [i, nums.index(desiredNumber)]
            i += 1
        return []