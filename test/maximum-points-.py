# 접근방식 생각하기
# k개의 카드를 선택하는데 왼쪽끝하고 오른쪽 끝에서만 선택할수있음 
# 마치 stack에서 pop을 해가는 느낌? 
# 맥시멈 k개를 구하니까 한쪽으로 다 쏠릴 경우를 생각해서
# 양쪽으로 k짜리 stack을 만든 다음 계속 비교하면서 pop을 하면 되려나?
# 근데 그 경우에는 그 다음 숫자까지 고려할 수 없음 

# 일단 k가 같은경우는 그냥 sum을하면됨

from re import I


class solution :
    def maxScore ( self, cardPOints : List [int], k : int ) -> int :
        if k == len(cardPOints) :
            return sum(cardPOints)
        

        
        return 1
