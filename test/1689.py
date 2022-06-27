class Solution:
    def minPartitions(self, n: str) -> int:
        maxNum = 0
        rst = 0
        for val in n :
            if int(val) > maxNum : maxNum = int(val)     
        return maxNum        

#a = Solution()
#print( a.minPartitions("27346209830709182346") )
