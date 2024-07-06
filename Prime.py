if __name__ == "__main__":
    x = int(input('Enter a number : '))

    for i in range(2,x):
        if x%i == 0:
            print('Number is not prime...')
            break
    else:
        print('Number is prime')
