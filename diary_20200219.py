[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
['spam', 2.0, 5, [10, 20]]

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)
# ['Cheddar', 'Edam', 'Gouda'] [17, 123] []

print(cheeses[0])
# Cheddar

numbers[1] = 5
print(numbers)
# [17, 5]

print('Edam' in cheeses)
# True
print('Brie' in cheeses)
# False

for cheeses in cheeses:
    print(cheeses)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print(numbers[i])
# 34
# 10

for x in empty:
    print('This never happens')

# LIST OPERATIONS
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
# [1, 2, 3, 4, 5, 6]

print([0] * 4)
# [0, 0, 0, 0]
print([1, 2, 3] * 3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
# ['b', 'c']
print(t[:4])
# ['a', 'b', 'c', 'd']
print(t[3:])
# ['d', 'e', 'f']
print(t[:])
# ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
# ['a', 'x', 'y', 'd', 'e', 'f']

t = ['a', 'b', 'c']
t.append('d')
print(t)
# ['a', 'b', 'c', 'd']

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
# ['a', 'b', 'c', 'd', 'e']

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
# ['a', 'b', 'c', 'd', 'e']

t = ['a', 'b', 'c']
del t[1]
print(t)
# ['a', 'c']
t.remove('a')
print(t)
# ['c']

t = ['d', 'c', 'e', 'b', 'a']
del t[1:5]
print(t)
# ['d']

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))

""" 6
74
3
154
25.666666666666668 """

""" total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average) """

""" numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average) """

s = 'spam'
t = list(s)
print(t)
# ['s', 'p', 'a', 'm']

s = 'pining for the fjords'
t = s.split()
print(t)
# ['pining', 'for', 'the', 'fjords']

s = 'spam-spam-spam'
delimeter = '-'
print(s.split(delimeter))
# ['spam', 'spam', 'spam']

t = ['pinning', 'for', 'the', 'fjords']
delimeter = ' '
print(delimeter.join(t))
