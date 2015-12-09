'''
str1, str2, str3 = 'amr', 'ali', 'alaa'
if str1 < str2:
    print('gogo')
else:
    print('lolo')
'''


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def primes(num=1):
    while True:
        if isprime(num):
            yield num
        num += 1


for number in primes():
    if number > 100:
        break
    print(number)
