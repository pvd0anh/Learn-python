class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # kiểm tra list rỗng
        if len(nums) == 0:
            return 0
        
        # nếu số tiếp theo khác số hiện tại thì tăng số đếm khác nhau lên 1
        # gán giá trị biến tạm cho số mới nhất
        # tiếp tục đến với số tiếp theo
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i +=1
                nums[i] = nums[j]
        return i + 1
