class Solution:
    def reverseWords(self, s: str) -> str:
        sList = list(s)
        revList = []
        word = []
        returnStr = ""

        for i in range(len(sList)):
            if sList[i] != ' ':
                word.append(sList[i])

                if i + 1 < len(sList):
                    if sList[i + 1] == ' ':
                        revList.append(word)
                        word = []
                else:
                    revList.append(word)
                    word = []

        for i in range (len(revList) - 1, -1, -1):
            returnStr += "".join(revList[i])
            if i != 0:
                returnStr += " "
        
        return returnStr
    

# Second solution
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         sList = s.split()
#         sList = sList[::-1]
#         return " ".join(sList)
