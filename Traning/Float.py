x = 5 
y = float.fromhex('A')
y = 0xA # hexadecimal
y = 0o12 # octal (python 2 uses 012)
y = 0b1010 # binary 
print ('x =', x, ',','y =',y )
print('x =', x, ',', y =', y')
print ('x.as_integer_ratio() =', x.as_integer_ratio())
print ('y.hex() =', )


#FOR LOOP 



# The for loop executes a suite of code for each element 

for elem in range (5) :
    print(elem, end= ' ')
print()
for elem in range (1,6) :
    print(elem, end='')
print()   

for elem in range(5,-1,-1):
    print('Countdown:',elem)


for char in 'string' :
    print(char, end=' ')
print()

for tup in (1, 3, 5):
    print(tup)

for val in ('Hey','hi','whoa') :
    print(val)

#INT



# The for loop executes a suite of code for each element 

for elem in range (5) :
    print(elem, end= ' ')
print()
for elem in range (1,6) :
    print(elem, end='')
print()   

for elem in range(5,-1,-1):
    print('Countdown:',elem)


for char in 'string' :
    print(char, end=' ')
print()

for tup in (1, 3, 5):
    print(tup)

for val in ('Hey','hi','whoa') :
    print(val)


#MATHS




x = 5 
y = 10 

x,y = 5.0, 10
print('x =', x, ',','y =', y)

from cmath import e, pi
import math

# The math module provides a couple of constante 
pi = math.pi
e = math.e
print(' The value of pi is:', pi)
print('The Rounded value of pi is:', round (pi,4))

# The float class allows creation of special numbers
pos_inf = float('inf')
neg_inf = float('-inf')
not_a_num = float('nan')

# The math module provide functions to detect numbers 
print ('math.isinf (pos_inf) =', math.isinf(pos_inf))
print ('math.isinf (neg_inf) =', math.isinf(neg_inf))
print ('math.isinf (not_a_num) =', math.isinf(not_a_num))

#beware that these special numbers propagate with erros 
print ('pos_inf * x =', pos_inf * x)
print ('neg_inf / y =', neg_inf / y)
print ('pos_inf + neg_inf=', pos_inf + neg_inf)
print ('not_a_num - y =', (not_a_num - y))


#WHILE LOOP



# The while loop executes a suite of code if its condition is true 

from msilib import PID_LASTSAVE_DTM
from unittest import result


counter = 3 
while counter > 0 :
    print('never executes suite')
    print('when condition is False')
    counter -= 1

while counter > 0:
    print('Never executes suite ')
    print('When condition is False')

    while 1 :
        print('Executes at least once ')
        if not counter :
            break

names = ['Bruno ', 'Nicoli']
while names:
    print(names.pop(), 'is going')

result = [1, 0, 1]
processed = 0 
passed = 0 
while result :
    processed +=1
    result = result.pop()
    if not result:
        continue
    passed += 1 
else:
    print('Processed:',processed,'Passed:', passed)