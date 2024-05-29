class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
           s=str(x)
           return s==s[::-1]