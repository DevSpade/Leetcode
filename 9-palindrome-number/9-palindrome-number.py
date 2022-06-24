class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is a negative number it is not a palindrome
        # If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
        if x < 0 or (x > 0 and x%10 == 0):   
            return False
        
        reversed = str(x)[::-1]
        b = int(reversed)
        if x == b :
            return True
        else :
            return False