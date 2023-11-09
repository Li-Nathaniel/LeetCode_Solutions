class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        for c in s:
            sDict[c] += 1
        
        for c in t:
            if c not in sDict:
                return False
            elif sDict[c] - 1 < 0:
                return False
            else:
                sDict[c] -= 1

        for c in sDict:
            if sDict[c] != 0:
                return False

        return True
