#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        int rParInd = min(min(s.find(')'), s.find(']')), s.find('}'));
        if (rParInd<1) return false;
        int lParInd = rParInd-1;
        switch (s[rParInd])
        {
            case ')':
                if (s[lParInd]!='(') return false;
                break;
            case ']':
                if (s[lParInd]!='[') return false;
                break;
            case '}':
                if (s[lParInd]!='{') return false;
                break;
        }
        s = s.substr(0, lParInd) + s.substr(rParInd+1);
        if (!s.empty()) return isValid(s);
        else return true;
    }
};

int main() {
    Solution s;
    cout << s.isValid("[(({})}]");
    // cout << s.isValid("()[]{}");
}