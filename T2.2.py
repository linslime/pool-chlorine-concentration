import math
from scipy import integrate

t0 = 0
t1 = 6
t2 = 9
t3 = 15

def func(x):
    print("x=",x)       #用于展示quad()函数对func的多次调用
    return math.cos(2*math.pi*x)*math.exp(-x)+1.2

def temperature(t):
    t = t + 9
    temperature = 0
    if t >= t0 and t <= t1:
        temperature = 26.8+9*math.cos(math.pi*(t+9-16.1766)/(-20.70924))
    elif t < t2:
        temperature = 26.8+9*math.cos(math.pi*(t-16.09216)/(9.400335))
    elif t < t3:
        temperature = 26.8+9*math.cos(math.pi*(19-16.09216)/(9.400335))*math.exp(-(t-19)/2.28546)
    return temperature
def t(t):
    return t
fArea,err = integrate.quad(temperature,0.7,4)
print("Integral area:",fArea,err)