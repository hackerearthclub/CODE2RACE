#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	string s;
	cin>>s;
	s = "00" + s;
	for(int i=0;i<s.size();i++)
		for(int j=i+1;j<s.size();j++)
			for(int k=j+1;k<s.size();k++){
				int x =  (s[i]-'0')*100 + (s[j] - '0')*10 + (s[k]-'0');
				if(!(x%8)){
					cout << "YES\n" << x;
					return 0;
				}
			}
	cout << "NO";
	return 0;
}
