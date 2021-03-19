class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # mé, đọc cái đề muốn loạn, ko hiểu nó đang nói cái j, phải google mới hiều
        # đại ý là: cộng 1 vào vị trí cuối cùng (*), nếu dư ra thì dồn lên vị trí nhỏ hơn, cho đến hết, có thể tăng độ dài của list. 
        # cộng theo kiều:
        # 1+ 1 = 2
        # 2+1 = 3
        # 9+1 = 0 dư 1 dồn lên số kế trước
        plus = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + plus
            print(digits[i] == 10)
            if digits[i] == 10:
                digits[i] = 0
                plus = 1
            else:
                plus = 0
        if plus == 1:
            digits[:] = [1] + digits
        print(plus)
        return digits
