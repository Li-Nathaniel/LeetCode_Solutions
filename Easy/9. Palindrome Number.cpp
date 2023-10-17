class Solution {
public:
    bool isPalindrome(int x) {
        string xString = to_string(x);
        int endIndex = xString.length() - 1;

        for (int i = 0; i < xString.length() / 2; i++) {
            if (xString.at(i) != xString.at(endIndex)) {
                return false;
            }

            endIndex--;
        }

        return true;
    }
};