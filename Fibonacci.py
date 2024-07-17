if __name__ == "__main__":
    n = int(input('Enter length of the series : '))
    a = 1
    b = 2
    
    print(a,end=" ")
    print(b,end=" ")
    
    i = 1
    
    while i<n-1:
        c = a+b
        print(c,end=" ")
        a = b
        b = c
        i += 1
        
    
    