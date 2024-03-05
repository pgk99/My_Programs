from array import *

val = array('i',[87,56,11,99,24])

def IsSorted(val):
    for i in range(0,4):
        if val[i]<=val[i+1]:
            continue
        else:
            return False
            break
    return True


def BubSort(val):
    tmp=0
    for i in range(0,4):
        if val[i]>val[i+1]:
            tmp = val[i+1]
            val[i+1] = val[i]
            val[i] = tmp


while(not IsSorted(val)):
    BubSort(val)


print("Below is the sorted array : ")


for i in val:
    print(i,end=" ")