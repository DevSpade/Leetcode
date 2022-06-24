class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   
            return False
        
        reversed = str(x)[::-1]
        b = int(reversed)
        if x == b :
            return True
        else :
            return False