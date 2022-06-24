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
                table[num] = i

```
# 먼저 dictionary를 생성
table = {}
```

```
# 그 뒤에 하나씩 배열을 접근하면서, 목표값과 현재값의 차이를 저장한 
# complement를 값을 구한다. 
# 이 값을 구하는 이유는 dict에 해당 값이 있으면 그게 정답이기 때문이다.
for i, num in enumerate(nums):
    complement = target - num
```

```
# 그 뒤는 사실 간단하다. dict를 순환하면서 해당 값이 있으면 해당 인덱스를 현재 인덱스와
# 같이 가져오면 된다.
# 그리고 만약에 값이 없다면 dict에 현재 값을 저장을 하고 넘어간다. 
if complement in table:
    return [i, table[complement]]
else:
    table[num] = i
```

