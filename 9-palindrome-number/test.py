import re


a = 1243421
#a = 111111
rst = len(str(a))
print(rst)

reversed = str(a)[::-1]
b = int(reversed)
print(b)
if a == b :
    print("Pass")
else :
    print("Nope")