class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        result = []
        for i in range(len(people)):
            h, k = people[i]
            result.insert(k, [h, k])
        
        return result
                
