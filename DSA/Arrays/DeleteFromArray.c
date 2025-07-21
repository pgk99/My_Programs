#include<stdio.h>

int main()
{
    int arr[20],n;
    printf("Enter size of Array : ");
    scanf("%d",&n);

    printf("Enter array elements : ");

    for (int i = 0; i < n; i++)
    {   scanf("%d",&arr[i]);    }

    
    //Deleting an element from an array

    printf("Enter the element u want to delete : ");
    int x,index,c=0;
    scanf("%d",&x);    

    for (int i = 0; i < n; i++)
    {   
        if (arr[i] == x)
        {   index = i;
            c++;
            break;
        } 
    }


    if(c)
    {
        for (int i = index; i<n-1; i++)
        {
            arr[i] = arr[i+1];
        }

        for (int i = 0; i < n-1; i++)
        {
            printf("%d ",arr[i]);
        }
    }
    
    else
        {   printf("Element not found. No need to delete");     }

    
    return 0;
}


