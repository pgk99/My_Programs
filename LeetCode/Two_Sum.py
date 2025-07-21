from array import *

if __name__ == "__main__":
    val = array('i',[])
    N = int(input('Enter array size : '))

    for i in range(N):
        x = int(input())
        val.append(x)

    target = int(input('Enter the required sum : '))

    output = []

    for i in range(N):
        for j in range(i+1,N):
            if val[i]+val[j] == target:
                output.append(i)
                output.append(j)
                break        
    
    print(output)

