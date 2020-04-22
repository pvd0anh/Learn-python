class Palindrome:
    @staticmethod
    def is_palindrome(word):
        # Please write your code here.
        if len(word) % 2 == 0:
            return False
        for i in range(int(len(word) / 2)):
            if word[i].lower() != word[len(word) - 1 - i].lower():
                return False
        return True


word = input()
print(Palindrome.is_palindrome(word))
# test:
>>> Palindrome.is_palindrome("Mom")
True
>>> Palindrome.is_palindrome("rotator")
True
