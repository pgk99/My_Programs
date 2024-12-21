#Reverse a String

if __name__ == "__main__":
    name = input('Enter String : ')
    
    for i in range(len(name)-1,-1,-1):
        print(name[i],end="")
