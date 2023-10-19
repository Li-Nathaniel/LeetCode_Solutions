class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelsList = []
        sList = list(s)

        for letter in sList:
            if letter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                vowelsList.append(letter)

        for i, letter in enumerate(sList):
            if letter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                sList[i] = vowelsList.pop()
        
        return "".join(sList)