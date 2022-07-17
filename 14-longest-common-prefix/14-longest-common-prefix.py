class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=[]
        for x in zip(*strs):
            if len(set(x)) == 1:
                result.append(x[0])
            else:
                break
        return "".join(result)