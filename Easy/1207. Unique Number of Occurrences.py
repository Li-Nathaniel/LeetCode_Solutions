class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrDict = {}
        for num in arr:
            if num not in arrDict:
                arrDict.update({num:1})
            else:
                arrDict[num] += 1

        revDict = {}
        for key, value in arrDict.items():
            if value not in revDict:
                revDict.update({value:1})
            else:
                revDict[value] += 1
        
        for val in revDict.values():
            if val > 1:
                return False
        
        return True