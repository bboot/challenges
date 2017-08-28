// 2017-8-23
// After a bit of study, next attempt at this
// Find the longest word in the dictionary that can be completely composed of
// subwords from the same dictionary
//
// I solved this with a trie-like concept
// 1. Create a std::set of all the words (called lsorted_), sorted on size
// 2. Create a std::set (called map_) of the words that are unique (i.e., not
//    completely composed of subwords from the input list)
// 3. Iterate the sorted set.
//    a. For each, if it can be entirely composed of subwords already in
//       map_, then add it to the queue (called q_) of longest words.  As words
//       are added, the smallest drop off the front to maintain qlen_ depth
//    b. Otherwise, add it to map_ as a unique  word
// Space: O(2N)
// Time: O(N^2) - could be significantly reduced by using memoization, see
// comment in code below.
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>

using namespace std;

// debug output
struct Dout {
    bool debug_{false};
    Dout& operator()(bool indent) {
        if (debug_) {
            if (indent) cout << '\t';
        }
        return *this;
    }
    template<class T>
    Dout& operator<<(T t) {
        if (debug_) {
            cout << t;
        }
        return *this;
    }
    Dout& operator<<(ostream& (*f)(ostream& o)) {
        if (debug_) {
            cout << f;
        }
        return *this;
    }
};
Dout dout;

// sort string by size first, else if equal length,
// then lexicographically
struct lcompare {
    bool operator() (const string& s1, const string& s2) const {
        if (s1.size() == s2.size()) {
            return s1 < s2;
        }
        return s1.size() < s2.size();
    }
};

class Words {
  public:
    explicit Words(string filename);
    virtual ~Words() {}
    void dump();
    void result();
  private:
    set<string, lcompare> lsorted_;
    set<string> map_;
    queue<string> q_; // maintain qlen=2 (front 2 longest words)
    int qlen_;
    string longest_;
    bool can_create(const string& w);
    void update_stats(const string& w);
};

void Words::update_stats(const string& w) {
    // if allow ties, use w.size >= q.back
    // otherwise, use w.size > q.back
    if (q_.empty() || w.size() >= q_.back().size()) {
        q_.push(w);
        dout << "pushing " << w << " onto queue" << endl;
        while (q_.size() > qlen_) {
            q_.pop();
        }
    }
}

// can_create() returns:
// true - can be created from subwords
// false - cannot be created from what is currently here.  should be
//         added
bool Words::can_create(const string& w) {
    if (!w.size()) {
        return true;
    }
    for (unsigned int i=0; i<=w.size(); i++) {
        string pref = w.substr(0, i);
        if (map_.find(pref) != map_.end()) {
            string suff = w.substr(pref.size(), w.size());
            dout << w << "=[" << pref << "]";
            // optimization possible here.
            if (can_create(suff)) {
                if (suff.empty()) {
                    dout << "; ";
                } else {
                    dout << "[" << suff << "]";
                }
                return true;
            } else {
                dout << "no " << suff;
            }
            dout << endl;
        }
    }
    return false;
}

Words::Words(string filename) : qlen_(15) {
    ifstream infile(filename);
    string word;
    while (infile >> word) {
        if (word.size() > longest_.size()) {
            longest_ = word;
        }
        lsorted_.insert(word);
    }
    for (auto w: lsorted_) {
        if (can_create(w)) {
            update_stats(w);
        } else {
            // the whole word can't be made of subwords so add it
            map_.insert(w);
        }
    }
}

void Words::result() {
    cout << "Longest word in dict: " << longest_
         << "{" << longest_.size() << "}" << endl;
    while (!q_.empty()) {
        string w = q_.front();
        cout << w << "{" << w.size() << "}" << endl;
        q_.pop();
    }
}

void Words::dump() {
    for (string s:  lsorted_) {
        cout << s << endl;
    }
}

int main(int argc, char *argv[]) {
    Words w("words.txt");
    //Words w("words_test.txt");
    w.result();
    return 0;
}
