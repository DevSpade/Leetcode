class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        diff = 0
        if len(nums) == 1 :
            return True
        elif len(nums) < 4 :
            beforeOneval = nums[0]
            for v in nums[1:] :
                if(v-beforeOneval) < 0 :
                    diff += 1
                beforeOneval = v
        else :
            beforeTwoVal = nums[0]
            beforeOneVal = nums[1]
            firstStat = 0
            secondStat = 0
        
            for v in nums[2:] :
                if (v-beforeTwoVal) < 0 :
                    if firstStat == 0 :
                        print(v)
                        print("here1")
                        diff += 1       
                if (v-beforeOneVal) < 0 :
                    print(v)
                    print("here2")
                    diff += 1
                    firstStat = 1
                else :
                    firstStat = 0
                beforeTwoVal = beforeOneVal
                beforeOneVal = v
        print(diff)
        if diff > 1 :
            return False
        else :
            return True