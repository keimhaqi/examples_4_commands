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

        vector<string> rows(min(numRows, int(s.size())));
        int curRow = 0;
        int director = 0; // 0 -> down, 1 -> up;
        for(char c : s){
            rows[curRow].push_back(c);

            if(curRow == 0){
                director = 0;
            }

            if(curRow == numRows - 1){
                director = 1;
            }

            if(director == 0){
                curRow++;
            }

            if(director == 1){
                curRow--;
            }
        }


        string ret = "";
        for(string str : rows){
            ret += str;
        }

        return ret;
    }
};

int main(){
    Solution solution;
    string str;
    str = "PAYPALISHIRING";
    cout << solution.convert(str, 3) << endl;
}
