a = 'a'
str = ''
limit = int(input('Enter a limit:'))
while len(str) < limit:
    str += a
    print(str)
else:
    print('The loop is over')
print('Out of the loop')