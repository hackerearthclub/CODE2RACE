#include<iostream.h>
#include<conio.h>
#include<stdio.h>
void main()
{ clrscr();
char string[20],c;
int i=0,num=0;
double prosum=1;
cout<<"Enter String:	";
gets(string);
while(string[i]!='\0')
{ num=0;
 num=(int)string[i];
 cout<<" "<<num<<"\n ";
 prosum=prosum*(num);
 cout<<prosum<<" ";
 i++;

}
cout<<prosum	;
getch();
}