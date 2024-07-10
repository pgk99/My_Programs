#Find the difference between the inter-digit product and sum of a given number
 
if __name__ == "__main__":
    
    x = int(input('Enter a number : '))
    sum = 0
    prod = 1
    
    while x!=0:
        rem = x%10
        sum = sum+rem
        prod = prod*rem
        x = x//10
        
    print(prod-sum)

