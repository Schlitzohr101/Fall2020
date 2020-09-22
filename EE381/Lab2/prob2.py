import numpy as np

def nSidedDie(p):
    sumCheck = 0
    for n in p:
        sumCheck = sumCheck + n
    if sumCheck != 1:
        print('The probabilities do not add up to 1.0')
        return

    rand = np.random.random()
    x = 0
    for counter, n in enumerate(p):
        if  rand >= x and rand < x + n:
            break
        x += n
    return counter

def genrecbit(S, e0, e1):
    bit = -1
    if S == 1:
        bit = nSidedDie([e1,1-e1])
    else:
        bit = nSidedDie([1-e0,e0])
    return bit

def cond_prob(n):
    p0 = 0.6
    p1 = 1 - p0
    e0 = 0.05
    e1 = 0.03

    failures = 0
    for i in range(n):
        #S = nSidedDie([p0,1-p0])
        S = 1
        R = genrecbit(S, e0, e1)
        if S != R:
            failures += 1
    return failures
print("Probability of P(R=1|S=1) ",end='')
print("%.5f"%(cond_prob(100000)/100000))