import math

import matplotlib.pyplot as plt

pi = math.pi
print(pi)
dim = 30 # 0-29 dim
v = []
idx = []
R=1

def doublefac(n):
    if n<=0:
        return 1
    else:
        return n * doublefac(n-2)

for i in range(dim):
    idx.append(int(i))
    # if i % 2 == 0:
    #     V = ((R**i)*pi**((i-1)/2))/(math.factorial(i/2))
    #     v.append(V)
    if i % 2 == 0:
        V = ((R ** i)*pi**(i / 2))/(math.factorial(int(i/2)))
    else:
        V = ((R ** i) * pi ** (i / 2)) / (math.sqrt(pi)*doublefac(i)/(2**((i+1)/2)))

    v.append(V)
print(v)
plt.figure(figsize=(10,6))
plt.plot(idx,v,'o')
plt.axis([0,dim,0,8])
plt.xticks(idx)
plt.xlabel('Dimension')
plt.ylabel('Elements') 
plt.show()
