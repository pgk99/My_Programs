from array import *


#Function to check whether array is sorted or not
def IsSorted(val):
    for i in range(0,n-1):
        if val[i]<=val[i+1]:
            continue
        else:
            return False
            break
    return True


#Bubble Sort
def BubSort(val):
    tmp=0
    for i in range(0,n-1):
        if val[i]>val[i+1]:
            val[i],val[i+1] = val[i+1],val[i]


#Driver code
if __name__ == "__main":
    val = array('i',[])
    n = int(input('Enter number of array elements : '))

    for i in range(n):
        x = int(input('Enter array values'))
        val.append(x)


    while(not IsSorted(val)):
        BubSort(val)


    print("Below is the sorted array : ")

    for i in val:
        print(i,end=" ")
