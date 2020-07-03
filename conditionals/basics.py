while True:
    res = int(input('Enter a number:'))
    if res == 0:
        print('0')
    elif res % 2 == 0:
        print('Par')
    else:
        print('Impar')