#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
	void print_vec(map<int, vector<int>>& m) {
		cout << "======================" << endl;
		for (auto it: m) {
			cout << "m[" << it.first << "]=";
			for (auto i: it.second) {
				cout << i << ",";
			}
			cout << endl;
		}
	}

    bool isPossible(vector<int>& nums) {
        //map<int, priority_queue<int>> m;
        map<int, priority_queue<int, vector<int>, greater<int>>> m;
        for (int x : nums) {
            int y = 1;
            if (m[x - 1].size()) {
                y += m[x - 1].top();
                m[x - 1].pop();
            }
            m[x].push(y);
        }
        for (auto it : m) {
            if (it.second.size() && it.second.top() < 3) return false;
        }
        return true;
    }
};

int main(int argc, char* argv[]) {
	Solution s;
	//vector<int> v = {1,2,3,3,4,4,5,6,7};
	vector<int> v = {1,2,3,3,4,4,5};
	cout << "is possible? " << s.isPossible(v) << endl;
	return 0;
}
