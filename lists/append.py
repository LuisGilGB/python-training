list = []

while True:
    newVal = input('Enter something (enter "break" to stop the loop):')
    if (newVal == 'break'):
        break
    list.append(newVal)
    print(list)
print("You've finished the enter process.")
print(list)