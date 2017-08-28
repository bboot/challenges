#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    unordered_map<int, int> a;
    int dfs(int i, int s) {
        if (a.find(i) == a.end()) {
            return 0;
        }
        s += a[i];
        int l = dfs(i+i+1, s);
        int r = dfs(i+i+2, s);
        if (!l && !r) {
            return s;
        }
        return l + r;
    }

    int pathSum(vector<int>& nums) {
        for (auto n: nums) {
            int t = n % 100;
            int v = n % 10;
            int p = (t - v) / 10;
            int d = (n - t) / 100;
            a[int(pow(2, (d-1)))-1 + (p-1)] = v;
        }
        return dfs(0, 0);
    }
};

/*
tests = [[113, 215, 221],
         [111, 212, 223, 314, 325, 336, 347],
         [111,217,221,315,415],
         [113,229,349,470,485],
        ]
*/

int main(int argc, char* argv[]) {
    Solution s = Solution();
    //vector<int> v = {113, 215, 221};
    vector<int> v = {111,212,223,314,325,336,347};
    cout << "result is: " << s.pathSum(v) << endl;
    return 0;
}

/*
class Solution(object):
    ''' leetcode runtime: 55 ms '''
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [None for i in xrange(32)]
        for n in nums:
            t = n % 100
            v = n % 10
            p = (t - v) / 10
            d = (n - t) / 100
            a[2**(d-1)-1 + (p-1)] = v
        def dfs(i, s):
            if a[i] == None:
                return 0
            s += a[i]
            l = dfs(2*i + 1, s)
            r = dfs(2*i + 2, s)
            if l == 0 and r == 0:
                return s
            return l + r
        s = dfs(0, 0)
        return s

*/
