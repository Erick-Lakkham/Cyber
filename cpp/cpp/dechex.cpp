#include <iostream>
#include "stdc++.h"
//#include <bits/stdc++.h>
using namespace std;

int main()
{

    int i;
    cout << "Enter an integer: ";
    cin >> i;

    stringstream ss;
    ss << hex << i;
    string res = ss.str();
    cout << "0x" << res << endl;

    return 0;

}
