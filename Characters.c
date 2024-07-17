#include <stdio.h>
int main()
{
    /*Characters from A to Z, we'll use ACII values....*/
    int i;

    for (i = 65;i <= 90; i++)
        {
            printf("%c ",i);
        }

    /*Characters from a to z, we'll use ASCII values*/
    for (i = 97; i <= 122; i++)
    {
        printf("%c ",i);
    }
    
    return 0;
}

