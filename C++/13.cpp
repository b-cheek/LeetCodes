#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> rNumVals;
        rNumVals['I'] = 1;
        rNumVals['V'] = 5;
        rNumVals['X'] = 10;
        rNumVals['L'] = 50;
        rNumVals['C'] = 100;
        rNumVals['D'] = 500;
        rNumVals['M'] = 1000;
        int ans = 0;
        for (int i = 0; i<s.length(); i++)
        {
            ans += rNumVals[s[i]];
            if (rNumVals[s[i+1]]>rNumVals[s[i]])
            {
                ans -= 2*rNumVals[s[i]];
            }
        }
        return ans;
    }
};