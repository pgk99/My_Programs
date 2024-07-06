if __name__ == '__main__':
    n = int(input('Enter a number : '))

    dummy = n
    rev = 0

    while n>0:
        rem = n%10
        rev = rev*10+rem
        n = n//10


    if rev == dummy:
        print('Given mumber is a palindrome..')
    else:
        print('Given mumber is not a palindrome..')
