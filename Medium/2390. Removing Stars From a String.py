class Solution:
    def removeStars(self, s: str) -> str:
        de = deque()

        for c in s:
            if c == '*':
                de.pop()
            else:
                de.append(c)
        
        return "".join(de)