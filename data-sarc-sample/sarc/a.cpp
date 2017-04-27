#include <bits/stdc++.h>
#include <fstream>
using namespace std;
int main()
{
	ifstream f,q;
	f.open("list.txt");
	string g,h;
	ofstream of;
	of.open("combined.txt");
	while(!f.eof())
	{
		f>>g;
		q.open(g.c_str());
		while(!q.eof())
		{
			q>>h;
			of<<h<<" ";
		}
		of<<endl;
		q.close();
	}
	f.close();
	of.close();
	return 0;
}