#include<iostream.h>
#include<conio.h>
#include<math.h>
int maze[7][7]={{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1}};


int path[7][7]={{1,1,1,1,1,0,1},
		{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1},
		{1,1,1,0,0,1,1},
		{1,1,1,1,1,1,1},
		{1,1,1,1,1,1,1}};
int cordinates[3][16],cordinates2[3][16];
void weightage(int x, int y, char Facing)
{
  int i,j,count=0;
     for(i=0; i<7; i++)
	{ for(j=0; j<7; j++)
	   {
		maze[i][j]=path[i][j];
	   }
	}

for (i=0; i<7; i++)
   {
    for (j=0; j<7; j++)
       { if (Facing=='N'||Facing=='S')
	 {
	   count=abs(y-j)+(2*abs(x-i));
	   path[i][j]=count;
	 if (Facing=='N')
	 { if (maze[i][j-1]==0)
	   {
	   path[i][j]+=5;
	   }
	 }
	  if(Facing=='S')
	 {
	  if (maze[i][j+1]==0)
	   {
	   path[i][j]+=5;
	   }
	 }
       }
      else if(Facing=='E'||Facing=='W')
	 {
	   count=(2*abs(y-j))+abs(x-i);
	   path[i][j]=count;
	   if (Facing=='E')
	    { if (maze[i-1][j]==0)
	      {
		path[i][j]+=5;
	      }
	    }
	    if(Facing=='W')
	    {
	      if (maze[i+1][j]==0)
	      {
		path[i][j]+=5;
	      }
	    }
	 }
       }
   }
   for(i=0; i<7; i++)
   {
    for(j=0; j<7; j++)
    {
      if(maze[i][j]==0)
       { path[i][j]=0;
       }
    }
   }
  path[x][y]=-1;
  cout<<"path == \n";
  for (i=0; i<7; i++)
  {
    for(j=0; j<7; j++)
    {  cout<<path[i][j]<<"   ";
    }
    cout<<endl;
  }
}


void search()
{ int i, j,p=0,size=0;
int temp=0, temp1=0, temp2=0;
 for(i=0; i<7; i++)
 { for(j=0; j<7; j++)
   { if(maze[i][j]==-1)
     { path[i][j]=-1;
     }
   }
 }
 for(i=0; i<7; i++)
   { for(j=0; j<7; j++)
    { if (maze[i][j]==0)
       {if(path[i-1][j]!=0&&(i-1>=0))
       {
       cordinates[0][p]=i-1;
       cordinates[1][p]=j;
       cordinates[2][p]=path[i-1][j];
       p++;
	}
       if(path[i][j-1]!=0&&(j-1>=0))
      { cordinates[0][p]=i;
       cordinates[1][p]=j-1;
       cordinates[2][p]=path[i][j-1];
       p++;
       }
       if(path[i+1][j]!=0&&(i+1<=6))
      { cordinates[0][p]=i+1;
       cordinates[1][p]=j;
       cordinates[2][p]=path[i+1][j];
       p++;
       }
       if(path[i][j+1]!=0&&(j+1<=6))
      { cordinates[0][p]=i;
       cordinates[1][p]=j+1;
       cordinates[2][p]=path[i][j+1];
       p++;
       }
       }
 }
}
 size=p;
for(i=0; i<size; i++)
 { cordinates2[0][i]=cordinates[0][i];
  cordinates2[1][i]=cordinates[1][i];
  cordinates2[2][i]=cordinates[2][i];
}
temp2=50;
for(i=0; i<p; i++)
{if(cordinates[2][i]!=-1)
{
if(temp2>cordinates[2][i])
{ temp2=cordinates[2][i];
temp=cordinates[0][i];
temp1=cordinates[1][i];
}
}
}
cout<<"beta zara coordinates ka array dikha do: \n";
for(i=0; i<p; i++)
{
cout<<cordinates[0][i]<<"   "<<cordinates[1][i]<<"   "<<cordinates[2][i]<<endl;
}

cout<<"\n beta zara reachinf coordiunates btana : \n";
cout<<temp<<"  "<<temp1<<"  "<<temp2;
}
void main()
{ clrscr();
char c,q='y';
 int x=0,y=0;
 while(q=='y')
 {cout<<"\n\nEnter the starting x cordinate:";
  cin>>x;
  cout<<"\n\nEnter the starting y cordinate:";
  cin>>y;
  cout<<"\n\nEnter the facing:";
  cin>>c;
  clrscr();
  weightage(x,y,c);
  getch();
  clrscr();
  search();
  getch();
  cout<<"\n\nDo you want to continue:";
  cin>>q;
}
getch();
}
