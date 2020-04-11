# LOOPS AND INTERATIONS
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

largest = None
print('Before:', largest)
for i in [3, 41, 12, 9, 74, 15]:
    if largest is None or i > largest:
        largest = i
    print('Loop:', i, largest)
print('Largest:', largest)

smallest = None
print('Before:', smallest)
for i in [3, 41, 12, 9, 74, 15]:
    if smallest is None or i < smallest:
        smallest = i
    print('Loop:', i, smallest)
print('Smallest:', smallest)

# Exercise 1:
number = None
average = 0
count = 0
total = 0
while True:
    number = input('Enter a number: ')
    if(number == 'done'):
        print('Average:', average, 'Total:', total,'Count:', count)
        break
    else:
        try: 
            number = int(number)
            isinstance(number, int)
            total += number
            count += 1
            average = total / count
            continue
        except:
            print('Bad data!')
            continue

# Strings
fruit = 'banana'
letter = fruit[1]
print(letter) # 'a'

letter = fruit[0]
print(letter) # 'b'

length = len(fruit)
last = fruit[length - 1]
print(last)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for char in fruit:
    print(char)

s = 'Monty Python'
print(s[0:5]) # Monty
print(s[6:12]) # Python

fruit = 'banana'
fruit[:3] # ban
fruit[3:] # ana