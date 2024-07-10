from array import *

#Function to check whether Array is sorted or not 
def IsSorted(val):
    for i in range(n-1):
        if(val[i]<=val[i+1]):
            continue
        else:
            return False
            break
    return True

#Selection Sort
def SelectionSort(val):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if(val[j]<val[min]):
                min = j
                val[i],val[min] = val[min],val[i]
                

#Driver code            
if __name__ == "__main__":
    val = array('i',[])
    n=int(input('Enter number of array elements : '))

    print('Enter array values : ')

    for i in range(n):
        x=int(input())
        val.append(x)
    
    while(not IsSorted(val)):
        SelectionSort(val)
        
    for k in val:
        print(k,end=" ")
    
    



                
        
    
        



