# TwoSum

주요 포인트는 hash를 사용해서 시간 복잡도를 줄이는 것이다. 

python의 dictionary는 내부가 hash로 이루어져있다. 
시간 복잡도를 보면 다음과 같다. 

|연산|시간복잡도|기능|
|---|---|---|
|len(k)|O(1)|개수 리턴|
|a[key]|O(1)|해당 키 조회 및 value 리턴|
|a(key) = value |O(1)|key/value 삽입|
|key in k |O(1)|키가 존재 하는지 확인|


    def twoSum(self, nums, target):
        table = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return [i, table[complement]]
            else:
                table[num] = 

