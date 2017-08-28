#include <iostream>

using namespace std;

class MyCout 
{
public:
  MyCout& operator()(bool indent) { 
    if ( indent ) cout << '\t'; 
    return *this;
  }

  template<class T>
  MyCout& operator<<(T t) {
    cout << t;
    return *this;
  }

  MyCout& operator<<(ostream& (*f)(ostream& o)) {
    cout << f;
    return *this;
  };
};

int main()
{
  MyCout mycout;
  int x = 10;
  mycout(true)<< "test" << 2 << x << endl ;
}
