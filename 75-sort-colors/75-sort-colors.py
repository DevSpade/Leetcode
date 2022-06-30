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
        