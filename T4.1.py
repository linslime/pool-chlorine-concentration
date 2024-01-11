import math
import random
import numpy as np
import copy
from scipy import integrate

step = 0.001
step0 = 3

stp = 0.01

t0 = 0
t1 = 5
t2 = 15
t3 = 19
t4 = 24

Ta = 7
T0 = 29.8
tm0 = 15
tm00 = 15.33195
tm1 = 15.7447
tm2 = 14.979209
w1 = -19.561598
w2 = 13.500613

k = math.atan(math.pi *(t3 - tm00)/w2) * w2 / math.pi
mannumber = [521,521,521,521,521,521,521,521,521]

T = 1
AT = 0.999
resu = []

r = []

resulist = copy.deepcopy(mannumber)

def temperature(t):
    t = t
    temperature = 0
    if t >= t0 and t <= t1:
        t = t + 24
        temperature = T0 + Ta * math.cos(math.pi * (t3 - tm00) / w2) * math.exp((t3 - t) / k)
    elif t < t2:
        temperature = T0 + Ta * math.cos(math.pi * (t - tm1) / w1)
    elif t < t3:
        temperature = T0 + Ta * math.cos(math.pi * (t - tm2) / w2)
    elif t <= t4:
        temperature = T0 + Ta * math.cos(math.pi * (t3 - tm00) / w2) * math.exp((t3 - t) / k)
    return temperature

def mannumbercount(t):
    result = 0
    if t >= 9.0 and t < 10.0:
        result = mannumber[0]
    elif t >= 10.0 and t <= 11.0:
        result = mannumber[1]
    elif t >= 12.0 and t < 13.0:
        result = mannumber[2]
    elif t >= 13.0 and t <= 14.0:
        result = mannumber[3]
    elif t >= 15.0 and t < 16.0:
        result = mannumber[4]
    elif t >= 16.0 and t <= 17.0:
        result = mannumber[5]
    elif t >= 18.0 and t < 19.0:
        result = mannumber[6]
    elif t >= 19.0 and t < 20.0:
        result = mannumber[7]
    elif t >= 20.0 and t <= 21.0:
        result = mannumber[8]
    else:
        result = 0
    return result

def func(t):
    return math.pow(10.0,(t/5 - 5.4))

def jifen():

    num1 = 0
    i = 0
    while i <= t4:
        mesg[round(i/step)].append(num1)
        num1 += func(mesg[round(i/step)][0]) * step
        i += step


def qiujifen(x1,x2):
    fArea, err = integrate.quad(func, x1, x2)
    return fArea

def day():
    tt = 0
    A = 0.6
    a = -0.1129503
    b = -0.1129503
    ttt = 0
    B = -0.0004
    v = 0
    state = 0
    tempy = 0.6

    tempN = 0
    concentration = []
    while tt <= t4:
        if state == 1:
            tempy = A * math.exp(b * qiujifen(tt,ttt)) + B * mesg[round(tt/step)][1] * (tt - ttt) + 1.4754 * (tt - ttt)
            if tempy > 0.6:
                tempy = 0.6
        elif state == 0:
            tempy = 0.6


        vtemp = A * b * func(mesg[round(tt/step)][0]) * tempy + B * mesg[round(tt/step)][1]


        if vtemp + 1.4754 >= 0 and tempy >= 0.6:
            v = 0
            if state == 1:
                state = 0
                A = tempy
                ttt = tt
        else:
            v = vtemp + 1.4754
            if state == 0:
                state = 1
                A = tempy
                ttt = tt
        if mesg[round(tt/step)][1] != tempN:
            A = tempy
            ttt = tt
        tempN = mesg[round(tt/step)][1]
        concentration.append([tt,tempy])
        tt += stp
    return concentration

def newans():
    first = random.randint(2,5)
    second = random.randint(1,10)
    number = random.randint(1,20)
    if second >= 1 and second <= 3:
        second = 1
    else :
        second = 0
    return [first,second,number]

def gai(list):
    global mannumber
    global resulist
    copy.deepcopy(mannumber)
    if list[1] == 1:

        resulist[list[0]] = resulist[list[0]]+list[2]
        if resulist[list[0]] > 521:
            resulist[list[0]] = 521
    elif list[1] == 0:
        resulist[list[0]] = resulist[list[0]]-list[2]
        if resulist[list[0]] < 0:
            resulist[list[0]] = 0
    return resulist

def count(list):
    global r
    r = [1,1,1,1,1,1,1,1,1]
    for x in list:
        if x[1] < 0.4:
            if x[0] >= 9.0 and x[0] < 10.0:
                r[0] = 0
            elif x[0] >= 10.0 and x[0] <= 11.0:
                r[1] = 0
            elif x[0] >= 12.0 and x[0] < 13.0:
                r[2] = 0
            elif x[0] >= 13.0 and x[0] <= 14.0:
                r[3] = 0
            elif x[0] >= 15.0 and x[0] < 16.0:
                r[4] = 0
            elif x[0] >= 16.0 and x[0] <= 17.0:
                r[5] = 0
            elif x[0] >= 18.0 and x[0] < 19.0:
                r[6] = 0
            elif x[0] >= 19.0 and x[0] < 20.0:
                r[7] = 0
            elif x[0] >= 20.0 and x[0] <= 21.0:
                r[8] = 0
    num = 0
    for x in range(9):
        num += r[x] * mannumber[x]

    return num

def accept(df):
    global mannumber
    global resulist
    global T
    if df < 0:
        mannumber = copy.deepcopy(resulist)
    else:
        # a = random.randint(1,100000000)/100000000
        # if a <= math.exp(-1 * df / T):
        #     mannumber = copy.deepcopy(resulist)
        # else:
        resulist = copy.deepcopy(mannumber)
    T = AT * T

mesg = []
tt = 0
while(tt <= t4):
    mesg.append([temperature(tt),mannumbercount(tt)])
    tt += step
jifen()
list = day()
re = count(list)
resu.append([re,mannumber])
while T > np.power(10.0,-20):
    list = day()
    re = count(list)
    accept(resu[-1][0] - re)
    resu.append([re,mannumber,r])
    print([re,mannumber ,r])
    li = newans()
    gai(li)







