#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        vector<int>::iterator iter, j;
        for (iter=nums.begin(); iter != nums.end(); iter++) {
            for (j=iter + 1; j != nums.end(); j++) {
                if (*iter + *j == target) {
					cout << *iter << " + " << *j << " = " << target << endl;
                    v.push_back(iter - nums.begin());
                    v.push_back(j - nums.begin());
                    return v;
                }
            }
        }
        return v;
    }
};


void printv(vector<int> v) {
    cout << "[ ";
    for (auto i: v) {
        cout << i << " ";
    }
    cout << "]" << endl;
}

int main(int argc, char *argv[]) {
	Solution s;
	vector<int> input = {2, 5, 5, 11};
	vector<int> v = s.twoSum(input, 10);
	printv(v);
	return 0;
}
