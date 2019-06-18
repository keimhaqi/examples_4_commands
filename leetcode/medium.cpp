#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int size1 = nums1.size();
        int size2 = nums2.size();

        if(size1 == 0 && size2 == 0) return 0.0;
        if(size1 != 0 && size2 == 0){
            return (size1 % 2) == 0 ? 0.5 * (nums1[size1 / 2] + nums1[(size1 / 2) - 1]) : (double)nums1[size1 / 2];
        }else if(size1 == 0 && size2 != 0){
            return (size2 % 2) == 0 ? 0.5 * (nums2[size2 / 2] + nums2[(size2 / 2) - 1]) : (double)nums2[size2 / 2];
        }

        vector<int> short_vector = nums1;
        vector<int> long_vector = nums2;

        if(size1 >= size2){
            short_vector = nums2;
            long_vector = nums1;

            size1 = short_vector.size();
            size2 = long_vector.size();
        }

        int i_min = 0;
        int i_max = size1;
        int half_len = (size1 + size2 + 1) / 2;

        while(i_min <= i_max){
            int i = (i_min + i_max) / 2;
            int j = half_len - i;
            if(i < i_max && long_vector[j-1] > short_vector[i]){
                i_min = i + 1;
            }else if(i > i_min && long_vector[j] < short_vector[i-1]){
                i_max = i - 1;
            }else{
                int max_left = 0;
                if(i == 0){
                    max_left = long_vector[j-1];
                }else if(j == 0){
                    max_left = short_vector[i-1];
                }else{
                    max_left = long_vector[j-1] > short_vector[i-1] ? long_vector[j-1] : short_vector[i-1];
                }
                if((size1 + size2) % 2 == 1){
                    return max_left;
                }

                int min_right = 0;
                if(i == size1){
                    min_right = long_vector[j];
                }else if(j == size2){
                    min_right = short_vector[i];
                }else{
                    min_right = long_vector[j] > short_vector[i] ? short_vector[i] : long_vector[j];
                }

                return (max_left + min_right) / 2.0;
            }
        }

        return 0.0;
    }
};

int main(){

    Solution solution;
    vector<int> nums1 = {3};
    vector<int> nums2 = {-2,-1};
    cout << solution.findMedianSortedArrays(nums1, nums2) << endl;
    return 0;
}