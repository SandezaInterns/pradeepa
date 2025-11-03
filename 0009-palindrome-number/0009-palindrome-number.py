class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string = str(x)
        reverse_str = string[::-1]
        return string == reverse_str
