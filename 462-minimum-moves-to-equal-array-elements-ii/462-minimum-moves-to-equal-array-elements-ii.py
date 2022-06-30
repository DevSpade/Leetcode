class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 평균값으로 하면, best case가 될 수 없음 (분포때문에)
        # 따라서 전체 리스트를 정렬하고 중간 요소로 맞춘다.
        nums.sort()
        center = nums[len(nums)//2]
        count = 0 
        for num in nums :
            count += abs(num - center)
        return count
    
