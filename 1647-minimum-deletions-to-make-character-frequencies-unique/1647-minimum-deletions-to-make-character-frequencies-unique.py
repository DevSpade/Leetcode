class Solution:
    def minDeletions(self, s: str) -> int:
        dictionary = {}
        for alpha in s :
            if alpha in dictionary :
                dictionary[alpha] = dictionary[alpha]+1
            else :
                dictionary[alpha] = 1
        value_list = list(dictionary.values())
        s = set()
        rst = 0
        point = 0 
        while value_list :
            size = len(s)
            s.add(value_list[point])
            if len(s) > size or value_list[point] == 0 :
                #print(value_list[point])
                value_list.remove(value_list[point])
                #print(value_list)
            else :
                rst += 1
                value_list[point] -= 1

        return rst