import numpy as np
import matplotlib.pyplot as plt
from math import *
import time
import tracemalloc

start=time.perf_counter()
tracemalloc.start()

#settings
seed = 0.5
sumr = 0

# Using the above nested radical formula for g=phi_d
# or you could just hard-code it.
# phi(1) = 1.61803398874989484820458683436563
# phi(2) = 1.32471795724474602596090885447809
def phi(d):
  x=2.0000
  for i in range(10):
    x = pow(1+x,1/(d+1))
  return x

# Number of dimensions.
d=2

def tckRsp(n, x1, x2, y1, y2):
    etal = sqrt((x2 - x1)**2 + (y2 - y1)**2) / n
    g = phi(d)
    alpha = np.zeros(d)
    for j in range(d):
        alpha[j] = pow(1 / g, j + 1) % 1
    z = np.zeros((n, d))

    # This number can be any real number.
    # Common default setting is typically seed=0
    # But seed = 0.5 is generally better.
    for i in range(n):
        z[i] = (seed + alpha * (i + 0.5)) % 1

    x = [x1 + etal + (i[0] * (x2 - x1 -2*etal)) for i in z]
    y = [y1 + etal + (i[1] * (y2 - y1 -2*etal)) for i in z]
    z = [[x[i], y[i]] for i in range(len(x))]

    return(z)

def kulon2(z, x1, x2, y1, y2):
    etal = sqrt((x2 - x1)**2 + (y2 - y1)**2) / len(z)

    minr = 0

    j = 0

    kolic = 2**8 * exp(-0.02*len(z))
    k=(x2-x1)*(y2-y1)/4
    #k=4
    while minr<etal and j < kolic:
        minr = max(x2,y2)

        for g in range(len(z)):
            vec = [0, 0]
            for i in range(len(z)):
                if(i != g):
                    rst = sqrt((z[g][0]-z[i][0])**2 + (z[g][1]-z[i][1])**2)
                    #minr = min(minr, rst)
                    f = k/(rst**2)
                    vec[1] -= f * ((z[i][1]-z[g][1])/rst)
                    vec[0] -= f * ((z[i][0]-z[g][0])/rst)
            # TODO vert arr
            vec[0] += (k/((z[g][0]-x1)**2) - k/((z[g][0]-x2)**2))
            vec[1] += (k/((z[g][1]-y1)**2) - k/((z[g][1]-y2)**2))

            while(z[g][0]+vec[0]>x2 or z[g][0]+vec[0]<x1):  vec[0]/=2
            while (z[g][1] + vec[1] > y2 or z[g][1] + vec[1] < y1):  vec[1] /= 2

            z[g][0] += vec[0]
            z[g][1] += vec[1]

            #minr = min(minr, abs(z[g][0] - x1), abs(z[g][0] - x2), abs(z[g][1] - y1), abs(z[g][1] - y2))

        for g in range(len(z)):
            for i in range(len(z)):
                if (i != g):
                    rst = sqrt((z[g][0] - z[i][0]) ** 2 + (z[g][1] - z[i][1]) ** 2)
                    minr = min(minr, rst, abs(z[g][0] - x1), abs(z[g][0] - x2), abs(z[g][1] - y1), abs(z[g][1] - y2))

        j+=1
    global minrst
    minrst = minr
    print("kol:", j,"etal:", etal, "minr:", minr)
    return z

n=100
z=[]

x1 = 0
y1 = 0
x2 = 1000
y2 = 1000

z = tckRsp(n, x1, x2, y1, y2)


#while minrst > etal:

if n<=pow((x2-x1)*(y2-y1), 3/10):
    z = kulon2(z,x1,x2,y1,y2)

#    n+=1
#    z = tckRsp(n, x1, x2, y1, y2)
#    etal = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / len(z)
#    print(n)

#for i in z: print(*i)

x = [i[0] for i in z]+[x1, x1, x2, x2]
y = [i[1] for i in z]+[y1, y2, y1, y2]
colors = [0.44784722]*len(z)+[0.45784723]*4
area = [100]*(len(z)+4)
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

etal = sqrt((x2 - x1)**2 + (y2 - y1)**2) / len(z)
minrst = 100000000

for g in range(len(z)):
    for i in range(len(z)):
        if (i != g):
            rst = sqrt((z[g][0] - z[i][0]) ** 2 + (z[g][1] - z[i][1]) ** 2)
            sumr += rst + abs(z[g][0] - x1) + abs(z[g][0] - x2) + abs(z[g][1] - y1) + abs(z[g][1] - y2)
            minrst = min(minrst, rst, abs(z[g][0] - x1), abs(z[g][0] - x2), abs(z[g][1] - y1), abs(z[g][1] - y2))

print("minr:", minrst, "etal:", etal, "sumR:", sumr)
#print(len(z)-n, n)
print(f"Запрос: {time.perf_counter()-start}")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
