import random

mi, ma = 1, 6

while True:
    r = random.randint(mi, ma)
    print(r)
    if r == 6:
        break




def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))






def remove_odd(array):
    idx = 0
    offset = 0
    max_iter = len(array)
    while max_iter:
        n = array[idx-offset]

        if n % 2 != 0:
            offset += 1
            array.remove(n)

        idx += 1
        max_iter -= 1

tests = [[4,5,4], [4,5,4,7,9,11], [4,5,4,7,9,11,12,13]]
for test in tests:
    print(f'List Before --> {test}')
    result = remove_odd(test)
    print(f'List After --> {test}')
    print('===='*15)