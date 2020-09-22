import numpy as np
import matplotlib
import matplotlib.pyplot as plt


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


p = [.1, .15, .2, .05, .3, .1, .1]
nRolls = 10000

outcomes = [0] * (len(p))
for i in range(0, nRolls):
    r = nSidedDie(p)
    outcomes[r] = outcomes[r] + 1

print(outcomes)

plt.stem([1,2,3,4,5,6,7],outcomes,use_line_collection=True)
plt.title("Steam plot: # of Occurences per each side of 7-sided die")
plt.ylabel("# Occurences")
plt.xlabel("Sides of die")
plt.show()

for temp in outcomes:
    print(temp)