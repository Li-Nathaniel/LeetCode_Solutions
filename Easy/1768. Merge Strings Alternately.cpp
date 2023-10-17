class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string returnString = "";
        int word1Index = 0, word2Index = 0;

        while (word1Index < word1.length() || word2Index < word2.length()) {
            if (word1Index < word1.length()) {
                returnString += word1[word1Index];
                word1Index++;
            }

            if (word2Index < word2.length()) {
                returnString += word2[word2Index];
                word2Index++;
            }
        }

        return returnString;
    }
};