import matplotlib.pyplot as plt
import math 


def p(n,k,prob):
    return math.comb(n,k) * prob**k * (1-prob)**(n-k)



n = 10
prob = .1

k = [i for i in range(10)]


plt.bar(k,[p(n,k[i],prob) for i in range(10)])
plt.xlabel('x')
plt.ylabel('p(x)')
plt.show()

