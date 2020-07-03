myDict = {'elements': [], 'enteredElements': 0, 'dirty': False}

while True:
    i = input('Enter an element (enter "break" to exit):')
    if i == 'break':
        break
    myDict['elements'].append(i)
    myDict['enteredElements'] += 1
    myDict['dirty'] = True
print('Exit')
print(myDict)