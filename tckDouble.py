import matplotlib.pyplot as plt
from math import *
import time
import tracemalloc

start=time.perf_counter()
tracemalloc.start()

etal = 0

def tckDouble(x1, x2, y1, y2, r, n):
    z=[]
    flag = 0

    n = mindiv(x1, x2, y1, y2, r, n)

    if(n in range(3)):
        match n:
            case 0: return []
            case 1: return [[x1+(x2-x1)/2, y1+(y2-y1)/2]]
            case 2: return [[x1+(x2-x1)/4,y1+(y2-y1)/4],[x2-(x2-x1)/4,y2-(y2-y1)/4]]

    width = (abs(x2-x1)//r)
    heigh = (abs(y1-y2)//r)
    wi = (x2-x1)/width
    he = (y2-x1)/heigh

    if((width+1)*(heigh+1)==n): flag = 1

    match flag:
        #x*y
        case 1:
            z.append([[x1, y1]])
            for i in range(width):
                z[0].append([z[0][i][0]+wi, z[0][i][1]])
            for i in range(heigh):
                z.append([[z[i][x][0], z[i][x][1]+he] for x in range(width+1)])
        #cross
        case 0:
            z.append([[x1, y1]])
            for i in range(width):
                z[0].append([z[0][i][0] + wi, z[0][i][1]])

            for i in range(heigh):
                if i % 2 == 1:
                    z.append([[z[0][x][0], z[0][x][1]+he*(i+1)] for x in range(width+1)])
                else:
                    z.append([[z[0][x][0] + (wi/2), z[0][x][1]+he*(i+1)] for x in range(width)])

    out = []
    for i in z: out+=i
    return out

def kol(x1, x2, y1, y2, r, n):
    z = []
    flag = 0

    if (n in range(3)):
        match n:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2

    width = (abs(x2 - x1) // r)
    heigh = (abs(y2 - y1) // r)
    wi = (x2 - x1) / width
    he = (y2 - x1) / heigh

    if ((width + 1) * (heigh + 1) == n): flag = 1

    match flag:
        # x*y
        case 1:
            return n
        # cross
        case 0:
            z.append([[x1, y1]])
            for i in range(width):
                z[0].append([z[0][i][0] + wi, z[0][i][1]])

            for i in range(heigh):
                if i % 2 == 1:
                    z.append([[z[0][x][0], z[0][x][1] + he * (i + 1)] for x in range(width + 1)])
                else:
                    z.append([[z[0][x][0] + (wi / 2), z[0][x][1] + he * (i + 1)] for x in range(width)])

            out = []
            for i in z: out += i
            return len(out)

def mindiv(x1, x2, y1, y2, r, n):
    d = n-kol(x1, x2, y1, y2, r, n)
    if d ==0:   return n
    k = n
    for i in range(n-d, n):
        t = n-kol(x1, x2, y1, y2, r, i)
        if t<d:
            d = t
            k = i
    return k

n=200
z=[]

x1 = 0
y1 = 0
x2 = 300
y2 = 400

#190 край

r = 1
z = tckDouble(x1, x2, y1, y2, r, n)
etal = sqrt((x2 - x1)**2 + (y2 - y1)**2) / len(z)
while(len(z)>n):
    r+=1
    if(r==100):
        print(9)
    z = tckDouble(x1, x2, y1, y2, r, n)

x = [i[0] for i in z]+[x1, x1, x2, x2]
y = [i[1] for i in z]+[y1, y2, y1, y2]
colors = [0.44784722]*len(z)+[0.45784723]*4
area = [100]*(len(z)+4)
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

print(len(z)-n, n)
print(f"Запрос: {time.perf_counter()-start}")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
