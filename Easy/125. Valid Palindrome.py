class Solution:
    def isPalindrome(self, s: str) -> bool:
        sList = [c.lower() for c in s if c.isalnum()]

        if len(sList) == 0:
            return True
        
        firstHalfWord = ''.join(sList[:int(len(sList) / 2)])
        secondHalfWord = ''.join(sList[int(len(sList) / 2):] if len(sList) % 2 == 0 else sList[int(len(sList) / 2) + 1:])

        secondHalfWord = secondHalfWord[::-1]
        
        return firstHalfWord == secondHalfWord