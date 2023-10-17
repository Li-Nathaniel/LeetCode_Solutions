class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;
        for (int i = 0; i < accounts.size(); i++) {
            int accountWealth = 0;
            for (int j = 0; j < accounts[i].size(); j++) {
                accountWealth += accounts[i][j];
            }
            if (accountWealth > maxWealth) {
                maxWealth = accountWealth;
            }
        }

        return maxWealth;
    }
};