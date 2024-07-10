from array import *


#Linear Search Function
def LinearSearch(val):
    print('Enter element u want to search : ')
    k = int(input())

    for i in val:
        if i == k:
            print('Element {} found at index {}'.format(k,val.index(k)))
            break
    else:
        print('Sorry...element not present in the array')


#Driver Code
if __name__ == "__main__":
    val = array('i',[])
    n = int(input('Enter size of array : '))

    print('Enter array values : ')
    for i in range(n):
        x = int(input())
        val.append(x)

    
    LinearSearch(val)


