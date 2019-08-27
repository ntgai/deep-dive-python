# import this -> The Zen of python by Tim Peters

'''
Sequences: Lists(Mutable), Tuples(Immutable), Strings(Immutable)
Sets: 	   Sets(Mutable), Frozen Sets(Immutable)
Mappings:  Dictionaries
'''

'''
Phsyical lines of code (newline character)-> Logical lines of code (newline token)

MultiLine Statements, and Strings:
Implicit vs Explicit

Implicit:
[1, #comment
 2, #comment
 3]

 def func(a,
 		  b, #comment
 		  ):

 Explicit:
 if a \
 	and b \
 	and c:

indentation is not important in explicit multi-line
'''


# _var -> private, internal use, 	__var -> used in inheritance chains for same named var, 	__var__ -> system defined
# x < y -> x.__lt__(y)

# X if CONDITION else Y
# b = 'a>=5' if a>5 else 'a<5'


'''
def func1():
	return func2()

def func2():
	return func1()

func1() -> RecursionError: maximum recursion depth exceeded
'''


'''
from math import sqrt
fn = lambda x: sqrt(x)
fn(4) -> 2.0
'''

'''
loops can also use else condition

l = [1,2,3]
val = 4
idx = 0

while(idx<len(l)):
	if(l[idx]==val):
		break
	idx += 1
else:
	l.append(val)
'''

'''
checking username has more than 8 digits, and it is alphabatic and printable, if not than asking to enter again

min_length_username = 8

while TRUE:
	username = input("Please enter your username: ")
	if len(name)>=min_length_username AND name.isprintable() AND name.isalpha():
		break
print("Hello {0}".format("Correct username"))
'''

'''
enumerate()

s = "hello"
for i, val in enumerate(s):
	print(i, val) 

OR

s = "Hello"
for i in range(len(s)):
	print(i, s[i])


for loop has also else case, it works no break or continue happened in overall loop
'''

'''
>>> i, j = 2, 4
>>> for l in range(5):
...     i += 1
...     j -= 1
...     try:
...             i/j
...     except:
...             print("Zero Division Error")
...             break
...     finally:
...             print("always working")
... else:
...     print("else condition")

1.0
always working
2.0
always working
5.0
always working
Zero Division Error
always working


>>> for i in []:
...     print(i)
... else:
...     print("List is empty")
... 
List is empty

'''

'''
>>> list = [4,3,2,1]
>>> fn = lambda x: x*x
>>> for i, val in enumerate(list):
...     print("{0} is square index, {1} is square value".format(fn(i), fn(val)))
... 
0 is square index, 16 is square value
1 is square index, 9 is square value
4 is square index, 4 is square value
9 is square index, 1 is square value
'''