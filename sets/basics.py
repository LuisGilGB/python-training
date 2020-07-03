mySet = {'cosa1', 'cosa2', 5, 7, 'abc'}
print(mySet)
while True:
    i = input('Enter something (enter "break" to exit the loop):')
    if i == 'break':
        break
    mySet.add(i)
    print(mySet)
print('Exit')