// Check if entered number  is an armstrong number.

#include<stdio.h>
int main()
{
    int inp, result = 0, number, rem;

    printf("Enter a number: ");
    scanf("%d", &inp);

    number = inp;
    
//checks digit and then moves on to the next digit

    while (number!=0)
    {
        rem = number%10;
        result = result + (rem*rem*rem);
        number = number/10;
    }

    if (result == inp)
        printf("This is an Armstrong number.");
    else
        printf("This is not an Armstrong number");

    return 0;
}
