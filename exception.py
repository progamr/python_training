# Exception Handling

try:
    content = open('xline')
    for line in content.readlines():
        print(line)
except IOError as e:
    print('something bad happened {}'.format(e))
print('completing our code after the bad thing !')
