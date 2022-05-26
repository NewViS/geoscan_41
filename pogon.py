from math import *
import random
import matplotlib.pyplot as plt
import time
import tracemalloc

start=time.perf_counter()
tracemalloc.start()


xh = 0
yh = 0
zh = 0
xw = -2
yw = -2
zw = 250
vh = 20
vw = 20
fiw = 0
fih = 1.3
vz = 0
t = 0.05
r = 10
rz = 10
oz = 0
vmax = 60
print(xh, yh, xw, yw, fiw)

k = 0

#out = []
#aim = []
A = -1
B = 1

while sqrt((xh - xw) ** 2 + (yh - yw) ** 2 + (oz - zw) ** 2) > r and k < 1:
    rast0=(((oz - zw)** 2) ** 0.5)
    rast = (((xh - xw) ** 2 + (yh - yw) ** 2) ** 0.5)
    fiw = atan((xh - xw) / (yh - yw)) + pi * (yw > yh)
    fiwz = atan((oz - zw) / (yh - yw)) + pi * (yw > yh)
    #xh = xh + vh * t * sin(fih)
    #yh = yh + vh * t * cos(fih)
    xh += random.uniform(A, B)
    yh += random.uniform(A, B)

    xw = xw + vw * t * sin(fiw)
    yw = yw + vw * t * cos(fiw)

    zw = zw + vz * t * sin(fiwz)

    rast1 = (((xh - xw) ** 2 + (yh - yw) ** 2) ** 0.5)
    rast2 = (((oz-zw)**2)**0.5)

    #if((rast1-rast)<0 and vw < vmax and rast>r):
    #    vw += 1
    #if((rast2-rast0) < 0 and (((oz - zw)**2)**0.5) >rz):
    #    vz+=1


    k += 1
    print(xh, yh, xw, yw)

    #out.append([xw, yw])
    #aim.append([xh, yh])


#x = [i[0] for i in out] + [i[0] for i in aim]
#y = [i[1] for i in out] + [i[1] for i in aim]
#colors = [0.44784722]*len(out)+[0.45784723]*len(aim)
#area = [100]*(len(out)+len(aim))
#plt.scatter(x, y, s=area, c=colors, alpha=0.5)
#plt.show()

print(f"Запрос: {time.perf_counter()-start}")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()