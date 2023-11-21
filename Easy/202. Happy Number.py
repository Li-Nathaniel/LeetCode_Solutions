class Solution:
    def isHappy(self, n: int) -> bool:
        nSet = set()

        while n != 1:
            if n in nSet:
                return False
            nSet.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        
        return True