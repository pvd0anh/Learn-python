class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n # tránh trường hợp k > n
        nums[:]=nums[n-k:]+nums[0:n-k]
