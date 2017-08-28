#include <iostream>
#include <vector>

using namespace std;

void quicksort(vector<int>::iterator begin,
               vector<int>::iterator end) {
    if (end - begin < 2) {
        return;
    }
    // partitioning
    int pivot = *begin;
    vector<int>::iterator cur = begin + 1;
    for (auto iter=begin + 1; iter!=end;) {
        if (pivot > *iter) {
            iter_swap(cur, iter);
            cur++;
        }
        iter++;
    }
    iter_swap(cur - 1, begin);
    // sort the subs
    quicksort(begin, cur);
    quicksort(cur, end);
}

void printv(vector<int> v) {
    cout << "[ ";
    for (auto i: v) {
        cout << i << " ";
    }
    cout << "]" << endl;
}

int main(int argc, char* argv[]) {
    vector<int> v={ 5, 3, 1, 19, 2, 8, 4, 2, 7 };
    printv(v);
    quicksort(v.begin(), v.end());
    printv(v);
    return 0;
}
