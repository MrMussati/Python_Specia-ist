from timeit import timeit
import numpy    


n = 100_000_000

#for

def tempo_for(n):
    total = 0 
    for i in range(n):
        total = total + i
    return total

    print ('For loop')


  #sun numpy

def tempo_sum_numpy(n):
    return numpy.sum(numpy.arange(n))

    print('sum numpy loop',timeit('tempo_sum_num(n)','from__main__import tempo_sum_numpy', number= 1))