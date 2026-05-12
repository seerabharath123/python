
def Add1(a,b):
    return(a+b)
def Sub1(a,b):
    return(a-b)
def Pro1(a,b):
    return(a*b)
def Div1(a,b):
    return(a/b)
def FDiv1(a,b):
    return(a//b)

print(math.floor(-45.17))
print(math.floor(100.12))
print(math.floor(100.72))

math.fabs(x)
Return the absolute value of x.

Syntax:
math.fabs(x)

Example:
import math
print(math.fabs(-10.99))
print(math.fabs(10.99))
print(math.fabs(-100.01))

math.factorial(x)
Return x factorial. Raises ValueError if x is not integral or is negative.

Syntax:
math.factorial(x)

Example:
import math
print(math.factorial(5))

math.fsum(iterable)
Return an accurate floating point sum of values in the iterable. 

Syntax:
math.fsum()

Example:
import math
print(math.fsum([5,7,2,4]))
print(math.fsum({5,7,2,4}))
print(math.fsum((5,7,2,4)))

pow() Method: This method returns value of x to the power of y.

Syntax:
math.pow(x,y)

Example:
import math 
print(math.pow(100, 2))
print(math.pow(2, 4))
print(math.pow(3, 0))

Python Number round() Function
It returns x rounded to n digits from the decimal point.

Syntax
round( x [, n]  )

Example:
priprint(round(10.236,2))#10.24
nprint(round(10.234,2))#10.23
t(round(10.236,3))#10.236
print(round(10.990,1))#11.0
print(round(80.23456, 2))
print(round(100.5623, 3))

import random
x=[1,2,3,4,5]
print(random.choice(x))#1
print(random.choice(x))#3
print(random.choice(x))#5

Example:
import random
items=[1,2,3,4,5,6,7]
print(random.choice(items))
print(random.choice(items))
print(random.choice(items))

import operator
a=int(input("Enter Any Valid  Number: "))
b=int(input("Enter Any Valid  Number: "))
print(operator.lt(a, b))
print(operator.le(a, b))
print(operator.eq(a, b))
print(operator.ne(a, b))
print(operator.ge(a, b))
print(operator.gt(a, b))

Example
a=int(input("Enter Any Valid  Number: "))
b=int(input("Enter Any Valid  Number: "))
print(operator.__lt__(a, b))
print(operator.__le__(a, b))
print(operator.__eq__(a, b))
print(operator.__ne__(a, b))
print(operator.__ge__(a, b))
print(operator.__gt__(a, b))













