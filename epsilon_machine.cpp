//Script que calcula el epsilon de máquina

#include <iostream>
using namespace std;

int main()
{
    double epsilon = 1.0;
    while ( 1.0 + 0.5*epsilon )
    {
    	epsilon = 0.5*epsilon;
    	cout << epsilon <<endl;
        if (epsilon == 0.0) {
            break;
        }
    }
return 0;

}
