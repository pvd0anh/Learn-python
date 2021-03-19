class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Cach 1:
        s_nums = set(nums)
        if len(s_nums)<len(nums):
            return True
        else:
            return False
        # Cach 2:
        # hashNum = {}
        # for i in nums:
        #     if i not in hashNum:
        #         hashNum[i] = 1
        #     else:
        #         return True
        # return False
