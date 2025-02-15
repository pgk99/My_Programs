#include<stdio.h>

int main()
{
    /*Declare an Array..*/
    int arr[10],n;

    printf("Enter how many elements : ");
    scanf("%d",&n);

    printf("Enter array elements : ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&arr[i]);
    }

    /*Display array elements*/
    for (int i = 0; i < n; i++)
    {
        printf("%d ",arr[i]);
    }

    /*Insert an Element at a specified index*/
    int x;
    printf("\nEnter element to be inserted : ");
    scanf("%d",&x);

    int j;
    printf("Enter index value : ");
    scanf("%d",&j);

    for (int k = n-1; k>=j; k--)
        {   arr[k+1] = arr[k];  }

    arr[j] = x;

    /*Display array elements*/
    for (int i = 0; i < n+1; i++)
    {
        printf("%d ",arr[i]);
    }

    return 0;
}

