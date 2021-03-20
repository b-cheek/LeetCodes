#include <string>

using namespace std;

class Solution {
public:
    string defangIPaddr(string address) {
        string newAddr = "";
        for (char i: address) 
        {
            if (i == '.')
            {
                newAddr += "[.]";
            } 
            else newAddr.push_back(i);
        }
        return newAddr;
    }
};
