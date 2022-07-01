class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dictionary = {'0':0,
                     '1':0,
                     '2':0}
        for num in nums :
            dictionary[str(num)] = dictionary[str(num)] + 1
        
        point = 0
        for key,val in dictionary.items() :
            for i in range(val) :
                nums[point] = int(key)
                point += 1      
                
        # 이중 for loop는 좋은 답이 아님. for loop 하나만으로 푸는 방법이 있을듯 
        