import numbers

#Solution
class Solution(object):
    def twoSum(self, nums, target):
        table = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return [i, table[complement]]
            else:
                table[num] = i
#Set test case
def set_case(numbers,target) :
    rst_dict = {'numbers':numbers,'target':target}
    return rst_dict

case1 = set_case([2,4,2,1,3],5)
case2 = set_case

a = Solution()

print(case1)

for  i,num in enumerate(case1['numbers']) :
    print(i,num)


#a.twoSum(case1['numbers'],case1['target'])
#a.twoSum(1,)
