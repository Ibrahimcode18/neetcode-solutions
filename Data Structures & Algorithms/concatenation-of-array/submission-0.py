class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [x for x in nums]
        n = len(nums)
        for i in range(n):
            ans.append(nums[i])
        return ans
