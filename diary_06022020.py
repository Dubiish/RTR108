Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
======================= RESTART: /home/dubiish/test.py =======================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/dubiish/test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/dubiish/test.py', 'a': 10}
>>> 
======================= RESTART: /home/dubiish/test.py =======================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/dubiish/test.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/dubiish/test.py', 'a': 10, 'b': 1.1, 'c': 'd'}
>>> type(c)
<class 'str'>
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> print(4)
4
>>> type('Hello, World!')
<class 'str'>
>>> type(17)
<class 'int'>
>>> type(3.2)
<class 'float'>
>>> message = 'And now for something completely diferent'
>>> n = 17
>>> pi = 3.14
>>> print(n)
17
>>> print(pi)
3.14
>>> type(message)
<class 'str'>
>>> type(n)
<class 'int'>
>>> type(pi)
<class 'float'>
>>> 76trombones = 'big parade'
SyntaxError: invalid syntax
>>> more@ = 100000
SyntaxError: invalid syntax
>>> minute = 59
>>> minute / 60
0.9833333333333333
>>> minute = 59
>>> minute//60
0
>>> 17
17
>>> x + 17
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x + 17
NameError: name 'x' is not defined
>>> x = 10
>>> x + 17
27
>>> quotient = 7 // 3
>>> print(quotient)
2
>>> first = 'Test '
>>> second = 3
>>> print(first * second)
SyntaxError: invalid character in identifier
>>> print(first + second)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(first + second)
TypeError: must be str, not int
>>> first * second
SyntaxError: invalid character in identifier
>>> inp = input()
test
>>> print(inp)
test
>>> prompt = "test message"
>>> speed = input(prompt)
test messageabc
>>> print(abc)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(abc)
NameError: name 'abc' is not defined
>>> print(speed)
abc
>>> # comment
>>> a = 10 # comment behind
>>> a = 35
>>> b = 12.50
>>> c = a * b
SyntaxError: invalid character in identifier
>>> a*b
437.5
>>> c=a*b
>>> c
437.5
>>> for word in words
SyntaxError: invalid syntax
>>> for word in words print(word)
SyntaxError: invalid syntax
>>> for word in words
SyntaxError: invalid syntax
>>> 
>>> for word in words: print(word)
a
SyntaxError: invalid syntax
>>> month = 09
SyntaxError: invalid token
>>> prompt = "Enter your name: "
>>> name = input(prompt)
Enter your name: Chuck
>>> print("Hello" + name)
HelloChuck
>>> prompt1 = "Enter Hours: "
>>> prompt2 = "Enter rate: "
>>> hours = input(prompt1)
Enter Hours: 35
>>> rate = input(prompt2)
Enter rate: 2.75
>>> print("Pay: " + rate * hours)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print("Pay: " + rate * hours)
TypeError: can't multiply sequence by non-int of type 'str'
>>> print("Pay: " + (rate * hours))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print("Pay: " + (rate * hours))
TypeError: can't multiply sequence by non-int of type 'str'
>>> pay = rate * hours
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    pay = rate * hours
TypeError: can't multiply sequence by non-int of type 'str'
>>> type(rate)
<class 'str'>
>>> int(rate)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    int(rate)
ValueError: invalid literal for int() with base 10: '2.75'
>>> float(rate)
2.75
>>> int(hours)
35
>>> pay = rate*hours
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    pay = rate*hours
TypeError: can't multiply sequence by non-int of type 'str'
>>> pay=int(hours)*float(rate)
>>> print(pay)
96.25
>>> width = 17
>>> height = 12.0
>>> width//2
8
>>> width/2.0
8.5
>>> height/3
4.0
>>> 1+2*5
11
>>> quotient = 7 // 3
>>> print(quotient)
2
>>> remainder = 7 % 3
>>> print(remainder)
1
>>> 
