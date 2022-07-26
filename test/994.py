from typing import List
def orangesRotting(grid: List[List[int]]) -> int:
    fresh = set()
    rotten = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh.add(str(i) + str(j))
            elif grid[i][j] == 2:
                rotten.add(str(i) + str(j))
    test = fresh
    print(test)
    print(rotten)

    for 
a = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
orangesRotting(a)
