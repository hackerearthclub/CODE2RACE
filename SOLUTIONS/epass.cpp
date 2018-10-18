#include<bits/stdc++.h>
using namespace std;
 
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sl(n)       scanf("%lld", &n)
#define sll(a,b)    scanf("%lld %lld", &a, &b)
#define slll(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define D(x)        cerr << #x " = " << (x) << '\n'
#define DBG         cerr << "Hi" << '\n'
#define pb          push_back
#define PI          acos(-1.00)
#define xx          first
#define yy          second
#define eps         1e-9
 
typedef unsigned long long int ULL;
typedef long long int LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
 
 
inline int setBit(int N, int pos) { return N=N | (1<<pos); }
inline int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
inline bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }
 
//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction
 
char str[50], pass[600010];
string s;
vector<string>segment[110];
vector<pii>password;
map<string, int>M;
int n;
 
void print()
{
    for(int i = 0; i<n; i++)
    {
        for(auto s: segment[i])
            cout << s << " ";
        cout << endl;
    }
    puts("----------------");
    D(pass);
    for(auto p: password)
        cout << p.xx << " " << p.yy << endl;
    puts("Done");
}
/// password[a] ke match korte chai segment[b] er sathe
vector<int>prio({4,2,3});
bool match(pii &a, vector<string>&b)
{
    LL have = 1;
    int odd = 0, even = 0;
    if(b.back() == "odd")
    {
        if((a.xx%2) == 0)
            return false;
    }
    else if(b.back() == "even")
    {
        if((a.xx%2) == 1)
            return false;
    }
    else
    {
        if(M[b.back()] != a.xx)
            return false;
    }
    b.pop_back();
    for(auto s: b)
    {
        if(s == "odd")
            odd++;
        else if(s == "even")
            even++;
        else
        {
            have *= M[s];
            if(have > 1e9 || have == 0)
                return false;
        }
    }
    if(a.yy % have)
        return false;
//    D(even);D(odd);D(have);D(a.yy);
    int make = (a.yy/have);
//    D(make);
    if(even > 32)
        return false;
    LL twos = (1LL<<even);
    if(make%twos)
        return false;
    make /= twos;
//    D(make);
    for(auto i: prio)
    {
        while((make%i) == 0 && even)
        {
            make /= i;
            even--;
        }
    }
//    D(make);
    for(int i = 9; i>=3; i-=2)
    {
        while((make%i) == 0 && odd)
        {
            make /= i;
            odd--;
        }
    }
//    D(make);
    return (make == 1);
}
 
bool solve()
{
    int len = strlen(pass);
    int digit = pass[0] - '0';
    int cnt = 1;
//    D(pass);
    for(int i = 1; i<len; i++)
    {
        if( (pass[i]-'0') == digit)
            cnt++;
        else
        {
            password.pb({digit, cnt});
            digit = pass[i] - '0';
            cnt = 1;
        }
    }
    password.pb({digit, cnt});
//    D(password.size());
//    print();
    int i = 0, j = 0;
    for(; i<password.size(); i++)
    {
        bool ok = false;
        while(j < n)
        {
            if(match(password[i],segment[j]))
            {
                ok = true;
                j++;
                break;
            }
            else
                j++;
        }
        if(!ok)
            return false;
    }
    return true;
}
string bla[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
int main()
{
//    freopen("input.txt","r",stdin);
//    freopen("out.txt","w",stdout);
 
    for(int i = 0; i<10; i++)
        M[bla[i]] = i;
    int t;
    sf(t);
    for(int cs = 1; cs<=t; cs++)
    {
        int cnt = 0;
        bool ed = false;
        while(true)
        {
            scanf("%s",str);
            s = str;
            bool segEd = false;
            if(s.back() == ',' || s.back() == '.')
            {
                if(s.back() == '.')
                    ed = true;
                else
                    segEd = true;
                s.pop_back();
            }
            segment[cnt].pb(s);
            if(segEd)
            {
                cnt++;
                continue;
            }
            if(ed)
            {
                cnt++;
                break;
            }
        }
        n = cnt;
        int hudai;
        sf(hudai);
        scanf("%s",pass);
//        print();
        printf("Case %d: ",cs);
        if(solve())
            puts("MAY BE");
        else
            puts("NO");
        for(int i = 0; i<n; i++)
            segment[i].clear();
        password.clear();
    }
    return 0;
}
 
