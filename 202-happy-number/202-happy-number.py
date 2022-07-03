class Solution:
    def isHappy(self, n: int) -> bool:
        setNums = set()
        ## 굉장히 좋은 방식 같음 . 
        ## for 문법이랑 제곱근 반복에 대해서 인지할것
        while n not in setNums :
            setNums.add(n)
            n = sum([int(x) ** 2 for x in str(n)])           
            if n == 1:
                return True     
        return False