// on mac, gcc -std=c++0x -stdlib=libc++ -lc++ alien.cc
#include <iostream>
#include <map>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    Solution() : rules() {
    }

    int countUnique(const vector<string>& words) {
        int cnt=0;
        set<char> chars;
        for (auto it = words.begin(); it != words.end(); it++) {
            for (const char& c: *it) {
                chars.insert(c);
            }
        }
        return chars.size();
    }
    void getLexRules() {
         cout << "insert first";
         rules.insert(make_pair('w', 'r'));
         rules.insert(make_pair('e', 'r'));
#if 0
         rules.insert(pair<char, char>('e', 't'));
         rules.insert(pair<char, char>('r', 'f'));
         rules.insert(pair<char, char>('t', 'f'));
         rules.insert(pair<char, char>('r', 't'));
#endif
    }
    string alienOrder(vector<string>& words) {
        int cnt = countUnique(words);
        cout << cnt;
        getLexRules();
        multimap<char, char>::iterator it;
        for (it = rules.begin(); it != rules.end(); it++) {
            cout << it->first;
            auto loc = find(order.begin(), order.end(), it->first);
            if (loc == order.end()) {
                // not there
                auto comp = find(order.begin(), order.end(), it->second);
                if (comp == order.end()) {
                    // comp not there
                    order.push_back(it->second);
                } else {
                    // comp is there
                    order.erase(comp, order.end());
                    order.insert(loc + 1, *comp);
                }
            } else {
                // there
                auto comp = find(order.begin(), order.end(), it->second);
                if (comp == order.end()) {
                    // not there
                    order.push_back(it->second);
                }
            }
        }
        string output;
        return output;
    }
    multimap<char, char> rules;
    vector<char> order;
};

int main(int argc, char *argv[]) {
    Solution s;
    vector<string> input {
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    };
    string order = s.alienOrder(input);
    cout << "hello" << endl;
    cout << order;
    return 0;
}
