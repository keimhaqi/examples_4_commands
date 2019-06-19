//
// Created by zhenping on 6/19/19.
//

#include <iostream>
#include <climits>

using namespace std;

class Solution {
public:
    int reverse(int x) {

        int deno = 10;
        int ret_sum = 0;
        while(x != 0){
            int remainder = x % deno;
            if(ret_sum > INT_MAX / 10 || (ret_sum == INT_MAX && remainder > 7)) return 0;
            if(ret_sum < INT_MIN / 10 || (ret_sum == INT_MIN && remainder < -8)) return 0;
            ret_sum = ret_sum * 10 + remainder;
            x = x / deno;
        }

        return ret_sum;
    }
};

int main(){

    Solution solution;
    int input = -123;
    cout << solution.reverse(input) << endl;
    return 0;
}