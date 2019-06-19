//
// Created by zhenping on 6/19/19.
//

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) return s;
        vector<string> strs;
        for(int i = 0; i < numRows; i++){
            strs.push_back("");
        }

        int director = 0;
        vector<int> index;
        for(int j = 0; index.size() < 2 * numRows - 2; j++){
            if(j < numRows){
                index.push_back(j);
            }else{
                index.push_back(2 * numRows - 2 - j);
            }
        }

        int ind = 0;
        for(string::iterator iter = s.begin(); iter != s.end(); iter++){
            strs[index[ind]].push_back(*iter);
            ind++;
            if(ind >= index.size()){
                ind = 0;
            }
        }

        string ret = "";
        for(vector<string>::iterator iter = strs.begin(); iter != strs.end(); iter++){
            ret.append(*iter);
        }
        return ret;
    }
};

int main(){
    Solution solution;
    string str;
    str = "A";
    cout << solution.convert(str, 1) << endl;
}
