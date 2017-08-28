// g++ -std=c++11
#include <vector>
#include <iostream>

using namespace std;

void print_array(vector<int>& v) {
    for (auto i: v) {
        cout << i << " ";
    }
    cout << endl;
}

void
partition(vector<int>& v) {
    vector<int>::iterator i, opened = v.begin() + 1,
                            pivot = v.begin(),
                            closed = opened;
    for (i = opened; i != v.end(); i++) {
        if (*i < *pivot) {
            closed = opened;
            cout << "swapping i=" << *i << " and opened=" << *opened << endl;
            swap(*opened, *i);
            //iter_swap(opened, i);
            opened = closed + 1;
            cout << "AFTER i=" << *i << " closed=" << *closed << " opened=" << *opened << endl;
            print_array(v);
        }
    }
    cout << "swapping pivot=" << *pivot << " and closed=" << *closed << endl;
    swap(*pivot, *closed);
    //iter_swap(pivot, closed);
}

int main(int argc, char* argv[]) {
    vector<int> v {5, 3, 1, 6, 10, 8, 7};
    //vector<int> v {4, 7, 6, 5, 3, 2};
    //vector<int> v {10, 5, 3, 8, 15, 7};
    cout << "BEFORE PARTITION" << endl;
    print_array(v);
    partition(v);
    cout << "AFTER PARTITION" << endl;
    print_array(v);
    return 0;
}
