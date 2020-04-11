# LESSON 9 DICTIONARIES

eng2sp = dict()
print(eng2sp)
# {}


eng2sp['one'] = 'uno'
print(eng2sp)
# {'one': 'uno'}

eng2sp = {
    'one' : 'uno', 
    'two' : 'dos', 
    'three' : 'tres'
}
print(eng2sp)
# {'one': 'uno', 'two': 'dos', 'three': 'tres'}

print(eng2sp['two'])
# dos

#print(eng2sp['four'])
# KeyError: 'four'

print(len(eng2sp))
# 3

print('one' in eng2sp)
# True
print('uno' in eng2sp)
# False

vals = list(eng2sp.values())
print('uno' in vals)
# True

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
#{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
# Counts all letters in word and "saves" them in key:value pairs

counts = {
    'chuck' : 1,
    'annie' : 42,
    'jan' : 100
}
print(counts.get('jan', 0))
# 100
print(counts.get('tim', 0))
# 0

word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)
# Same result as previous implementation but in different way using the get method with default value 0

# FILES AND DICTIONARIES
""" fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts) """
# {'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'it': 1, 'is': 3, 'the': 2, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}

counts = {
    'chuck' : 1,
    'annie' : 42,
    'jan' : 100
}
for key in counts:
    print(key, counts[key])
# chuck 1
# annie 42
# jan 100

print()

for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
# annie 42
# jan 100

lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

# ['chuck', 'annie', 'jan']
# annie 42
# chuck 1
# jan 100

import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
# {'but': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'it': 1, 'is': 3, 'the': 2, 'east': 1, 'and': 3, 'juliet': 1, 'sun': 2, 'arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}

