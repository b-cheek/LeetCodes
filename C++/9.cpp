#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string intStr = to_string(x);
        string revStr = "";
        for (int i=intStr.length()-1; i>=0; i--)
        {
            revStr.push_back(intStr[i]);
        }
        return (intStr==revStr);
    }
};