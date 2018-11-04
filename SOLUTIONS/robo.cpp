#include<iostream>
#include<string>
using namespace std;
int main()
{
	long tc;
	int i, j, dot, num, len, flag,l, k;
	string s;
	cin>>tc;
	while(tc--)
	{
		k = 0;
		dot = 0;
		num = 0;
		flag = 0;
		cin>>s;
		len = s.length();
		int d[100], index[100];
		for(i = 0; i < len; i++)
		{
			if(s[i] == '.')
				dot++;
			else
			{
				num++;
			}
		}
		if(dot == len)
			cout<<"safe"<<endl;
		else if(num == 1)
			cout<<"safe"<<endl;
		else
		{
			for(i = 0; i < len; i++)
			{
				if(s[i] != '.')
				{
					d[k] = s[i]-'0';
					index[k] = i;
					k++;
				}
			}
			for(l = 0; l < k; l++)
			{
				for(j = index[l] - d[l]; j <= index[l] + d[l] && j < len; j++)
				{
					if(j < 0)
						continue;
					if(s[j] == -100)
					{
							flag = 1;
							break;
					}
					s[j] = -100;
				}
			}
			/*for(i = 0; i < len; i++)
				cout<<s[i]<<endl;*/
			if(flag == 1)
				cout<<"unsafe"<<endl;
			else
				cout<<"safe"<<endl;
		}
	}
}