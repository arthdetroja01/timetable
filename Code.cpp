                /**************************************
                *                                     *
                *            sasta_samurai            *
                *                                     *
                **************************************/
#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace chrono;
using namespace __gnu_pbds;
#define ll long long int
#define ld long double
#define cd complex<ld>
#define pi pair<int, int>
#define pl pair<ll,ll>
#define pd pair<ld,ld>
#define vi vector<int>
#define vs vector<string>
#define vd vector<ld>
#define vl vector<ll>
#define vpi vector<pi>
#define vpl vector<pl> 
#define vvl vector<vl> 
#define vcd vector<cd>
#define st string
#define ct continue
#define mll map<ll,ll>
#define loop(i,a,b) for(ll i=a;i<b;++i)
#define rloop(i,a,b) for(ll i=a;i>=b;i--)
#define in(a,n) for(ll i=0;i<n;++i) cin>>a[i];
#define pb push_back
#define mk make_pair
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define dis(v) for(auto i:v)cout<<i<<" ";cout<<endl;
#define display(arr,n) for(int i=0; i<n; i++)cout<<arr[i]<<" ";cout<<endl;
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);srand(time(NULL));
#define l(a) a.length()
#define maxx(a,b) max(1ll*(a),1ll*(b));
#define minn(a,b) min(1ll*(a),1ll*(b));
#define fr first
#define sc second
#define mod 1000000007
#define yes cout<<"YES"<<endl;
#define no cout<<"NO"<<endl;
#ifndef ONLINE_JUDGE
#define debug(x) cerr << #x<<" "; _print(x); cerr << endl;
#else
#define debug(x);
#endif
#define debug(x) cerr << #x<<" "; _print(x); cerr << endl;
void _print(ll t) {cerr << t;}
void _print(int t) {cerr << t;}
void _print(string t) {cerr << t;}
void _print(char t) {cerr << t;}
void _print(double t) {cerr << t;}
template <class T, class V> void _print(pair <T, V> p);
template <class T> void _print(vector <T> v);
template <class T> void _print(set <T> v);
template <class T, class V> void _print(map <T, V> v);
template <class T> void _print(multiset <T> v);
template <class T> void _print(queue <T> v) {cerr << "{"; while(v.size()){ _print(v.front()); cerr << " ";v.pop();} cerr << "}"; }
template <class T> void _print(stack <T> v) {stack<T> a; while(v.size()) a.push(v.top()), v.pop(); cerr << "{";  while(a.size()){ _print(a.top()); cerr << " ";a.pop();}  cerr << "}"; }
template <class T, class V> void _print(pair <T, V> p) {cerr << "{"; _print(p.fr); cerr << ","; _print(p.sc); cerr << "}";}
template <class T> void _print(vector <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(set <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(multiset <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T, class V> void _print(map <T, V> v) {cerr << "[ "; for (auto i : v) {_print(i); cerr << " ";} cerr << "]";}

template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
template<class key, class value, class cmp = std::less<key>>
using ordered_map = tree<key, value, cmp, rb_tree_tag, tree_order_statistics_node_update>;
ll add(ll x,ll y)  {ll ans = x+y; return (ans>=mod ? ans - mod : ans);}
ll sub(ll x,ll y)  {ll ans = x-y; return (ans<0 ? ans + mod : ans);}
ll mul(ll x,ll y)  {ll ans = x*y; return (ans>=mod ? ans % mod : ans);}

map<st,st> batch;
map<st,ll> batch_no;
map<st,vector<st>> cno;
vector<vector<map<string,vector<string>>>> courses(10,vector<map<string,vector<string>>>(10));
map<string,ll> days = {{"1MON",1},{"2TUE",2},{"3WED",3},{"4THU",4},{"5FRI",5}};
map<string,ll> hrs = {{"H1",1},{"H2",2},{"H3",3}};
ll hn,bn;
vvl days_required;
st print_space = "";
ofstream file1("timetable.txt");
void print(map<st,st> &m){
    for(auto m1 : m){
        file1<<left<<setw(5)<<m1.fr<<" "<<left<<setw(5)<<m1.sc<<endl;
    }
    file1<<"--------------------------------------------------------------------"<<endl;
}
void print(map<st,ll> &m){
    for(auto m1 : m){
        file1<<left<<setw(5)<<m1.fr<<" "<<left<<setw(5)<<m1.sc<<endl;
    }
    file1<<"--------------------------------------------------------------------"<<endl;
}
void print(map<st,vector<st>> &m){
    for(auto m1 : m){
        file1<<left<<setw(10)<<m1.fr<<" ";
        vector<string> vec = m1.sc;
        file1<<left<<setw(60)<<vec[0];
        file1<<left<<setw(10)<<vec[1];
        file1<<left<<setw(10)<<vec[2];
        file1<<endl;
    }
    file1<<"--------------------------------------------------------------------"<<endl;
}
void print(vector<vector<map<string,vector<string>>>> &m){
    for(auto h : hrs){
        for(auto b : batch){
            for(ll i = 1;i <= days_required[h.sc][batch_no[b.fr]];i++){
                file1<<left<<setw(5)<<h.fr<<" "<<left<<setw(30)<<b.sc<<" ";
                for(auto d : days){
                    if(courses[h.sc][d.sc][b.fr].size() >= i){
                        st temp = courses[h.sc][d.sc][b.fr][i-1];
                        file1<<left<<setw(20)<<temp<<setw(60)<<cno[temp][0]<<setw(10)<<cno[temp][1]<<setw(10)<<cno[temp][2];
                    }
                    else{
                        file1<<left<<setw(20)<<print_space<<setw(60)<<print_space<<setw(10)<<print_space<<setw(10)<<print_space;
                        // continue;
                    }
                }
                file1<<endl;
            }
        }
    }
    file1<<"--------------------------------------------------------------------"<<endl;
}

int main()
{
    ifstream file("time_table_program_output.csv");

    if(!file.is_open()) cout<<"File not open"<<endl;
    else{
        vector<st> vec;
        vector<vector<st>> data;
        st line,word;

        //loop(i,0,8) cout<<vec[i]<<endl;
        getline(file,line);
        ll cnt = 1;
        while(getline(file,line)){
            vec.clear();
            stringstream str(line);
            while(getline(str,word,',')) vec.push_back(word);
            batch[vec[2]] = vec[3];
            cno[vec[4]] = {vec[5],vec[6],vec[7]};
            courses[hrs[vec[1]]][days[vec[0]]][vec[2]].pb(vec[4]);
            data.push_back(vec);
            if(batch_no[vec[2]] == 0) batch_no[vec[2]] = cnt++;
        }
        hn = hrs.size();
        bn = batch.size();
        days_required = vvl (hn+10,vl (bn+10));
        for(auto h : hrs){
            for(auto b : batch_no){
                ll ele = 0;
                for(auto d : days){
                    ele = max(ele,courses[h.sc][d.sc][b.fr].size()*1ll);
                }
                days_required[h.sc][b.sc] = ele;
            }
        }
        print(batch);
        print(batch_no);
        print(days);
        print(hrs);
        print(cno);
        print(courses);
        // ll n = data.size();
        // cout<<n<<endl;
        // for(auto strs : data){
        //     for(auto str : strs) cout<<str<<" ";
        //     cout<<endl;
        // }
        // for(auto b : batch_no){
        //     cout<<b.fr<<" "<<b.sc<<endl;
        // }
        loop(i,0,hn+10){
            loop(j,0,bn+10) cout<<days_required[i][j]<<" ";
            cout<<endl;
        }
        file.close();
        file1.close();
    }
    return 0;
}

