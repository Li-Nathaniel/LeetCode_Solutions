class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) is 0:
            return True
        if len(t) is 0:
            return False
        
        for c in t:
            if len(t) is not 0 and c is s[0]:
                if len(s) is 1:
                    return True
                elif len(t) is 1:
                    return False
                else:
                    s = s[1:]
                    t = t[1:]
        
        if s is None:
            return True
        
        return False