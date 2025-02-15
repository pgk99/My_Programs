#include<stdio.h>

int main()
{
    int a = 1,b = 2,c;
    int n = 3;
    printf("%d %d",a,b);
    c = a+b;
    printf(" %d",c);

    while (n<15)
        {
            a = b;
            b = c;
            c = a+b;
            printf(" %d",c);
            n++;
        }
    return 0;
}



