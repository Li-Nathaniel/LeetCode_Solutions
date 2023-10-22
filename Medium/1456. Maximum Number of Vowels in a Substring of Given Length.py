class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lib = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        right = k - 1
        maxVowels = 0

        while right < len(s):
            maxVowels = max(maxVowels, sum(s[left:right + 1].count(c) for c in lib))
            left += 1
            right += 1

        return maxVowels

# Pasess all test cases but exceeds time limit