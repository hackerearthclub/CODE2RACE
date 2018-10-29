#include <iostream>
#define fastio ios_base::sync_with_stdio(false)
#define fastcin cin.tie(NULL)
using namespace std;

int main(){
      // For file input and output
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
      fastio;
      fastcin;
    int t;
cin>>t;
while(t--){
      string a;
      cin>>a;
      bool arr[a.length()];
      for(int i=0;i<a.length();i++){
            arr[i] = false;
      }
      int count = 0;
      for(int i=0;i<a.length();i++){
            if(a[i]=='.')
            continue;
            else
            {
                  for(int j=i;j>=max(0,(i)-(int(a[i])-48));j--){
                        if(arr[j]){
                              count = 1;
                              break;
                        }
                        else
                        {
                              arr[j] = true;
                        }
                  }
                  int n = a.length()-1;
                  int mini = min(n,i+(int(a[i])-48));
                  for(int k=i+1;k<=mini;k++){
                        if(arr[k]){
                              count = 1;
                              break;
                        }
                        else
                        {
                              arr[k] = true;
                        }
                  }
                  if(count==1){
                        break;
                  }
            
            }
      }
      if(count==1){
            cout<<"unsafe\n";
      }
      else
      {
            cout<<"safe\n";
      }
}
return 0;
}