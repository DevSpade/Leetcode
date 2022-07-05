from functools import cache


def a(one,two) :
    @cache
    def b(three,four) :
        print(three,four)
    [b(0, j) for j in range(3)]

a(1,2)



class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        for i in range(n) :
            if m == 0 :
                return n
            elif grid[]
        
        
        @cache
        def helper(r, c):
            if r == m:
                return c
            elif grid[r][c] == 1 and c+1 < n and grid[r][c+1] == 1:
                return helper(r+1, c+1)
            elif grid[r][c] == -1 and 0 <= c-1 and grid[r][c-1] == -1:
                return helper(r+1, c-1)
            else:
                return -1
            
        return [helper(0, j) for j in range(n)]