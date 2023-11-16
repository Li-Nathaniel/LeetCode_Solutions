class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        sDeque = deque()

        for bracket in s:
            if bracket in brackets.keys():
                sDeque.append(bracket)
            elif bracket in brackets.values():
                if len(sDeque) == 0:
                    return False
                if brackets[sDeque.pop()] != bracket:
                    return False

        if len(sDeque) > 0:
            return False
        
        return True