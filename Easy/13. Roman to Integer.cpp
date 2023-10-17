class Solution {
public:
    int romanToInt(string s) {
        int convertInt = 0;
        unordered_map <char, int> romans = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        for (int i = 0; i < s.length(); i++) {
            convertInt += romans[s.at(i)];
            if (i != 0 && s.at(i) != 'I') {
                if (((s.at(i) == 'V' || s.at(i) == 'X') && s.at(i - 1) == 'I') || ((s.at(i) == 'L' || s.at(i) == 'C') && s.at(i - 1) == 'X') || ((s.at(i) == 'D' || s.at(i) == 'M') && s.at(i - 1) == 'C')) {
                    convertInt -= (romans[s.at(i - 1)] * 2);
                }
            }
        }

        return convertInt;
    }
};