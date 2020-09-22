import numpy as np
import matplotlib
import matplotlib.pyplot as plt



#True is heads, False is Tails
def flipcoin():
    rand = np.random.random()
    return rand*10 >=5

def get50Heads():
    headAmount = 0
    for i in range(100):
        if flipcoin():
            headAmount += 1
    if headAmount == 50:
        return True
    return False
    

def solution3():
    wins = 0
    losses = 0
    for i in range(100000):
        if get50Heads():
            wins+=1
        else:
            losses+=1
    # plt.stem(["wins","losses"],[wins,losses],use_line_collection=True)
    # plt.show()
    return (wins/100000)*100


probability = solution3()
print("Probability of winning A Get 50 Heads game:",probability,"%")
