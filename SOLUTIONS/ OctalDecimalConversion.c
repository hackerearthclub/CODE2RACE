#include <stdio.h>
#include <math.h>

int convertDecimalToOctal(int decimalNumber);
long long convertOctalToDecimal(int octalNumber);
int main()
{
    int choice,decimalNumber,octalNumber;
    printf("Select what you want to convert:\n");
    printf("1. Decimal to Octal:\n");
    printf("2. Octal to Decimal:\n");
    scanf("%d",&choice);
    switch(choice)
    {
        case 1:
        printf("Enter a decimal number: ");
        scanf("%d",&decimalNumber);
        printf("%d in decimal = %d in octal", decimalNumber, convertDecimalToOctal(decimalNumber));
        break;
        
        case 2:
        printf("Enter an octal number: ");
        scanf("%d", &octalNumber);
        printf("%d in octal = %lld in decimal", octalNumber, convertOctalToDecimal(octalNumber));
        break;
        default :
        printf("Wrong choice!\n");



    }
    return 0;
}

int convertDecimalToOctal(int decimalNumber)
{
    int octalNumber = 0, i = 1;

    while (decimalNumber != 0)
    {
        octalNumber += (decimalNumber % 8) * i;
        decimalNumber /= 8;
        i *= 10;
    }

    return octalNumber;
}

long long convertOctalToDecimal(int octalNumber)
{
    int decimalNumber = 0, i = 0;

    while(octalNumber != 0)
    {
        decimalNumber += (octalNumber%10) * pow(8,i);
        ++i;
        octalNumber/=10;
    }

    i = 1;

    return decimalNumber;
}