import module
print(module.sum(10,20))

# next method

from module import *
print(sum(20,25))
print(mul(20,25)) 
# next method using alias
import module as m
print(m.sum(10,20))