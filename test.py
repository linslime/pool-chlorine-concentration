import math
from scipy import integrate




def function(x):
    y = x
    return y

fArea,err = integrate.quad(function,-4,4)
print(fArea,err)