class Solution {
public:
    int numberOfSteps(int num) {
        int steps = 0;
        for (int i = 0; num > 0; i++) {
            if (num % 2 == 0) {
                num /= 2;
            }
            else {
                num -= 1;
            }

            steps++;
        }

        return steps;
    }
};