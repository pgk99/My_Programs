from array import *


def PeakElement(val):
    max = val[0]
    for i in val:
        if i > max:
            max = i
    return max


def MinElement(val):
    min = val[0]
    for i in val:
        if i < min:
            min = i
    return min


#Driver code
if __name__ == "__main__":
    val = array('i',[])
    n = int(input('Enter array size : '))

    print('Enter array elements : ')
    for i in range(n):
        x = int(input())
        val.append(x)

    print("Largest element of the array is : ",PeakElement(val))

    print("Smallest element of the array is : ",MinElement(val))
    
