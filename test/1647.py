from typing import Set


a ="bbcebab"


def minDeletions(s: str) -> int :
    dictionary = {}
    for alpha in s :
        print(alpha)
        if alpha in dictionary :
            print("add")
            print(dictionary)
            dictionary[alpha] = dictionary[alpha]+1
            print(dictionary)
        else :
            print("new")
            dictionary[alpha] = 1
            print(dictionary)
    #sorted_dict = dict(sorted(dictionary.items(),key=lambda item: item[1]))
    value_list = list(dictionary.values())
    s = set()
    rst = 0
    point = 0 
    while value_list :
        size = len(s)
        s.add(value_list[point])
        if len(s) > size or value_list[point] == 0 :
            print("add: ", value_list[point])
            value_list.remove(value_list[point])
            print("removed list: ",value_list)
        else :
            rst += 1
            value_list[point] -= 1
    print(rst)
    return rst


minDeletions(a)
