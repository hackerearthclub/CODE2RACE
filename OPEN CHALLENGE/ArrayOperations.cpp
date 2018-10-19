#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
class arrays{
public:
    void input(int *&arr,int num);
    void insert_i(int *&arr,int num);
    void delete_i(int *&arr,int num);
    void show_i(int *&arr,int num);
    void sort_i(int *&arr,int num);
    void sort_s(int *&arr,int num);
    void search_l(int *&arr,int num);
    void search_b(int *&arr,int num);
};
void arrays::input(int *&arr,int num)
{   int i;
    srand(time(0));
	for(i=0; i<num; i++)
	{
		arr[i]=rand()%num+1;
    }}
void arrays::search_l(int *&arr,int num)
{   int a;
    cout<<"\nEnter Element to Search\t";
    cin>>a;
    for(int i=0;i<num;i++){
        if(arr[i]==a){
            cout<<"\n Element Found"<<endl;
            cout<<"\n Postion of Element is\t"<<i<<endl;
        }}}
 void arrays::search_b(int *&arr,int num){
     int a,first,last,middle;
    cout<<"Enter the umber that you want to search:\t";
    cin>>a;
	first = 0;
	last = num-1;
	middle = (first+last)/2;
	while (first <= last) {
	   if(arr[middle] < a) {
		first = middle + 1; }
	   else if(arr[middle] == a)
	   {
		cout<<a<<" found in the array at the location "<<middle+1<<"\n";
                break; }
           else {
                last = middle - 1; }
           middle = (first + last)/2;  }
        if(first > last){
	   cout<<a<<" not found in the array"<<endl;
	} }
void arrays::insert_i(int *&arr,int num)
{   int a,b,i;
    cout<<"Enter Position\t";
    cin>>a;
    cout<<"Enter Element\t";
    cin>>b;
    for(i=num;i>=a;i--){
        arr[i+1]=arr[i];}
    arr[a]=b;
    num++;
    }
void arrays::delete_i(int *&arr,int num){
int a;
cout<<"\nEnter position";
cin>>a;
for(int i=a;i<num;i++)
arr[i]=arr[i+1];
num--;
}
void arrays::sort_s(int *&arr,int num)
{
    int i,j,temp;
    cout<<"Sorting array using selection sort\n";
    for(i=0;i<num;i++) {
        for(j=0;j<num-1;j++) {
        if(arr[j]>arr[j+1]) {
        temp=arr[j];
        arr[j]=arr[j+1];
        arr[j+1]=temp;
        } } } }
void arrays::sort_i(int *&arr,int num){
    int i,j,temp;
    cout<<"Sorting array using insertion sort\n";
    for(i=1;i<=num-1;i++)
    {
        temp=arr[i];
        j=i-1;

        while((temp<arr[j])&&(j>=0))
        {
            arr[j+1]=arr[j];
            j=j-1;
        }

        arr[j+1]=temp;
    }
}
void arrays::show_i(int *&arr,int num){
for(int i=0;i<num;i++)
    cout<<arr[i]<<"\t";
    }
 int main(){
     arrays a;
     int num;
     cout<<"Enter Size of Array"<<endl;
     cin>>num;
     int *arr=new int[num];
     int o;
     int start,stop;

do{     cout<<"\n1. Input\t 2. Insert\t 3.Selection Sort \t 4. Insertion Sort \t 5. Linear Search \t 6.Binary Search \t 7. Show\t 8. Delete\t 9. Exit"<<endl;
        cout<<"\nEnter Number"<<endl;
        cin>>o;
switch(o){
    case 1:
        a.input(arr,num);
        break;
   case 2:
            a.insert_i(arr,num);
            break;
   case 3:
       start = clock();
        a.sort_s(arr,num);
     stop=clock();
        cout<<"Time for selection sorting is : "<<(stop-start)/double(CLOCKS_PER_SEC)<<" Seconds"<<endl;
        break;
   case 4:
        start = clock();
        a.sort_i(arr,num);
        stop=clock();
        cout<<"Time for insertion sorting is : "<<(stop-start)/double(CLOCKS_PER_SEC)<<" Seconds"<<endl;
        break;
   case 5:  start = clock();
            a.search_l(arr,num);
            stop=clock();
        cout<<"Time for linear search is : "<<(stop-start)/double(CLOCKS_PER_SEC)<<" Seconds"<<endl;
            break;
    case 6:
           start = clock();
            a.search_b(arr,num);
            stop = clock();
        cout<<"Time for binary search is : "<<(stop-start)/double(CLOCKS_PER_SEC)<<" Seconds"<<endl;
            break;
    case 7:
            a.show_i(arr,num);
            break;
    case 8:
        a.delete_i(arr,num);
        break;
    case 9:
        return 0;
}
}
while(1);
delete [] arr;
}
