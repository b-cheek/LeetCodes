#include <vector>

using namespace std;

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> runningSum;
        int sum=0;
        for (int i: nums)
        {
            sum+=i;
            runningSum.push_back(sum);
        }
        return runningSum;
    }
};