class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_list = list(s)
        k = set()
        point = 0 
        maxSeq = 0
        curSeq = 0
        while string_list :
            size = len(k)
            k.add(string_list[point])
            if len(k) > size :
                string_list.remove(string_list[point])
                curSeq += 1
                if maxSeq < curSeq : 
                    maxSeq = curSeq
            else :
                k=set()
                k.add(string_list[point])
                curSeq = 1
                string_list.remove(string_list[point])
        return maxSeq
