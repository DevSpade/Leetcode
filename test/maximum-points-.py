# 접근방식 생각하기
# k개의 카드를 선택하는데 왼쪽끝하고 오른쪽 끝에서만 선택할수있음 
# 마치 stack에서 pop을 해가는 느낌? 
# 맥시멈 k개를 구하니까 한쪽으로 다 쏠릴 경우를 생각해서
# 양쪽으로 k짜리 stack을 만든 다음 계속 비교하면서 pop을 하면 되려나?
# 근데 그 경우에는 그 다음 숫자까지 고려할 수 없음 

# 일단 k가 같은경우는 그냥 sum을하면됨
import types
from typing import List
class Solution() :
    def maxScore ( self, cardPOints : List[int], k : int ) -> int :
        if k == len(cardPOints) :
            return sum(cardPOints)
        max_sum = 0
        front = [0]
        back = [0]
        for i in range(k):
            front.append(front[-1]+cardPOints[i])
            back.append(back[-1]+cardPOints[-(i+1)])
        print(front)
        print(back)
        for i in range(k+1):
            max_sum = max(max_sum,front[i]+back[k-i])
            print(max_sum)
        return max_sum

a = Solution()
rst = a.maxScore([1,9,3,4,5,6,1],k=4)
#print(rst)

"""
b = [0,1]
print(b[-1])
b.append(b[-1]+10)
b.append(b[-1]+11)
b.append(b[-1]+12)
print(b)
"""