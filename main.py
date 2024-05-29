# lecture 03

numbers = []
contacts = list()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 11, 13]

contacts = ["John Doe", 1234567, "Some Sity", True]

print(numbers)
print(type(numbers))
tpl = ()
tup = tuple()

tup = ('a','b', 'c')
tpl = (1,2,3) # 1,2,3 (6,)
print(tup)

print(type(tup))

x = range(5)
print(x)
print(type(x))

print(range(-5, 5, 2))

print(list(range(-5, 5, 2)))
print(tuple(range(-5, 5, 2)))

my_tuple = tuple(range(-5, 5, 2))

print(my_tuple[2])

print((1,2,3) < (0,2,2))
# print((1,2,3) < [0,2,2]) # TypeError: '<' not supported between instances of 'tuple' and 'list'

print(list((1,2,3)) < [0,2,2])
print((1,2,3) < tuple([0,2,2]))

print(numbers.index(7))
print(numbers.index(5, 6, 12))

print("John Doe" not in contacts)

print(numbers.count(5))
print(min(numbers))
print(max(numbers))

print(max(tup)) # a b c 
print(id(numbers))
numbers += 8, 88, 88 
print(id(numbers))
print(numbers)

print(id(tpl))
tpl += 5, 55, 555
print(id(tpl))
print(tpl) # (1, 2, 3, 5, 55, 555)

for item in numbers:
    print(item)

for item in tpl:
    if item == 5:
        continue
    print(item)
else:
    print("All done!")

for item in tpl:
    if item == 55:
        break
    print(item)

index = 0
for item in numbers:
    print(index, item)
    index += 1

for index in range(len(numbers)):
    item = numbers[index]
    print(index, item)

for index, item in enumerate(numbers):
    print(index, item)

print(numbers[2:8])
print(numbers[:8])
print(numbers[1:10:2])

numbers.append(7777)
print(numbers)

numbers.extend([888, 555, 444])
print(numbers)

numbers.insert(4, 4444444)
print(numbers)
print(numbers.pop())
print(numbers)

print(numbers.pop(4))
print(numbers)

numbers.remove(888)
print(numbers)

del numbers[5]
print(numbers)

cache = [1, 2, 3, 4, 5, 7, 8, 9, 10, 5, 11, 13, 8, 88, 88, 7777, 555]
print(cache)
# cache[:] = []
cache.clear()
print(cache)

new_numbers = numbers
print(id(new_numbers))
print(id(numbers))
print(new_numbers)

copy_numbers = numbers[:]
print(id(numbers))
print(id(copy_numbers))
from copy import copy
copy_2_numbers = copy(numbers)
print(id(copy_2_numbers))
print(id(copy_numbers))

from copy import deepcopy

matrix = [
    [1,2,3],
    [4,5,6],
    [7,7,8]
]

matrix_copy = deepcopy(matrix)

print(id(matrix[0]) == id(matrix_copy[0]))
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

l = ['g', 'y', 'aaa', 'ab', 'bbbb', 'd', 'c']
l.sort()
print(l)

l.sort(key=len)
print(l)

fruits = ('apple', 'mango', 'papaya', 'cherry')

green, *tropic, red = fruits
print(green)
print(tropic)
print(red)

import random

print(random.random())
print(random.random())

print(random.randint(0, 10))
print(random.randint(5, 55))

print(random.choice(l))
print(random.choice(l))
print(random.choice(l))

random.shuffle(l)

print(random.choice(l))
print(random.choice(l))
print(random.choice(l))


