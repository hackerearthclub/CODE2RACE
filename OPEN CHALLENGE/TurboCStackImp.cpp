#include<iostream.h>
#include<conio.h>
enum Boolean{FALSE,TRUE};
class stack
{
	int a[10];
	int top;
	int maxsize;
 public:stack()
	{
		top=-1;
		maxsize=10;
	}
	stack(int max)
	{
		top=-1;
		maxsize=max;
	}
	Boolean Isfull();
	Boolean Isempty();
	void push(int);
	void pop();
	void top1();
	void disp();
 };

 Boolean stack::Isfull()
 {
	if(top==maxsize-1)
		return TRUE;
	return FALSE;
 }
 Boolean stack::Isempty()
 {
	if(top==-1)
		return TRUE;
	return FALSE;
 }
 void stack::push(int x)
 {
	if(Isfull())
		cout<<"\nstack is full";
	else a[++top]=x;
 }
 void stack::pop()
 {
	if(Isempty())
		cout<<"\nstack is empty";
	else cout<<"\npopped element is: "<<a[top--];
 }

 void stack::top1()
 {
	if(Isempty())
		cout<<"\nstack is empty";
	else cout<<"\ntop element is: "<<a[top];
 }

 void stack::disp()
 {
	if(Isempty())
		cout<<"\nstack is empty";
	else
	{	for(int i=top;i>=0;i--)
		{
			cout<<a[i]<<"\t";
		}
	}
 }
 void main()
 {
	stack s;
	int m,ch;

	cout<<"\nenter the max size of the stack:";
	cin>>m;

	s=stack(m);
	cout<<"\n enter the elements for the stack: ";
	do
	{
		cout<<"\n1.push\n2.pop\n3.top\n4. display\n0. exit";
		cout<<"\nenter your choice:";
		cin>>ch;
		switch(ch)
		{
			case 1: cout<<"\nenter element to be pushed";
				int ele;
				cin>>ele;
				s.push(ele);
				break;
			case 2: s.pop();
				break;
			case 3: s.top1();
				break;
			case 4: s.disp();
				break;
			case 0: break;
			default: break;
		}
	}while(ch!=0);
	getch();
 }
