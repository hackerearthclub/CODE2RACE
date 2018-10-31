#include<stdio.h>
int STACK[100],x,n,choice,top,i;
void push(void);
void pop(void);
void display(void);
int main()
{
	top=-1;
	printf("Enter the size of Stack[MaX_100]\n");
	scanf("%d",&n);
	printf("Which operarion do you want to perform \n");
	printf("--------------------------------------\n");
	printf("\n1. PUSH\n 2.POP\n3. DISPLAY\n4.EXIT\n");
	do
	{
		printf("Enter your choice\n");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
			{
				push();
				break;
			}
			case 2:
			{
				pop();
				break;
			}
			case 3:
			{
				display();
				break;
			}
			case 4:
			{
				printf("\n \tExit Point");
				break;
			}
			default:
			{
				printf("Enter valid choice(1/2/3/4)\n");
			}
		}
	}
	while(choice!=4);
	return 0;
}
void push()
{
	if(top>=n-1)
	{
		printf("Overflow occurs\n");
	}
	else
	{
		printf("Enter a value to be pushed\n");
		scanf("%d",&x);
		top++;
		STACK[top]=x;
	}
}	
void pop()
{
	if(top<=-1)
	{
		printf("UnderFlow occurs\n");
	}
	else
	{
		printf("The popped element is %d\n",STACK[top]);
		top--;
	}
}
void display()
{
	if (top>=0)
	{
		printf("The element in the stack are: \n");
		for(i=top;i>=0;i--)
		{
			printf("%d\n",STACK[i]);
			//printf("Enter next choice \n");
		}
	}
	else
	{
		printf("Your stack is empty \n");
	}
}










