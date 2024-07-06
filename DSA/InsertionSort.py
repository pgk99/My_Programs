from array import *
    
    
def IsSorted(arr):
    for i in range(n):
        if(arr[i]<=arr[i+1]):
            continue
        else:
            return False
        break
    return True


def InsertionSort(arr):
    for i in range(1,len): 
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        
      
      
if __name__ == "__main__":  
    arr = array('i',[])
    len = int(input('Enter number of array elements : '))
    n=len-1

    print('Enter array values : ')

    for i in range(len): 
        x = int(input())
        arr.append(x)

    while(not IsSorted(arr)):
        InsertionSort(arr)
    
     
    print("Below is the sorted array :")

    for i in arr:
        print(i,end=" ")
        



