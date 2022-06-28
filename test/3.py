def lengthOfLongestSubstring(s: str) -> int:
    string_list = list(s)
    k = set()
    point = 0
    maxSeq = 0
    curSeq = 0
    startPoint = 0

    while len(string_list) > point:
        size = len(k)
        k.add(string_list[point])

        if len(k) > size :
            curSeq += 1
            point += 1
            if maxSeq < curSeq : 
                maxSeq = curSeq
        else :
            k=set()
            curSeq = 0
            startPoint += 1
            point = startPoint

    return 

a = "abcabcbb"   
lengthOfLongestSubstring(a)