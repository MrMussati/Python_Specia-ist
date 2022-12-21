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
