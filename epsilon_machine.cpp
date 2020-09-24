//Script que calcula el epsilon de máquina

#include <iostream>
using namespace std;

int main()
{
    double epsilon = 1.0;
    while ( 1.0 + 0.5*epsilon != 1.0)
    {
    	epsilon = 0.5*epsilon;
    }
    cout << epsilon <<endl;
return 0;

}
