from math import *
import random
import matplotlib.pyplot as plt
import time
import tracemalloc

start=time.perf_counter()
tracemalloc.start()


xh = 0 #начальное положение цели
yh = 0 #
zh = 0 #
xw = -2 #начальное положние дрона
yw = -2 #
zw = 250 #
vh = 20 #скорость движения цели
vw = 20 #скорость движения дрона
fiw = 0 #угол между дроном и целью
fih = 1.3 #угол между траекторией цели и оХ в случае прямолиненого движения
vz = 0 #скорость изменения высоты дрона
t = 0.05 #изменение времени за один шаг
r = 10 #радиус в пределах которого дрон должен приблизиться к цели
rz = 10
oz = 0
vmax = 60
print(xh, yh, xw, yw, fiw)

k = 0

#out = []
#aim = []
A = -1
B = 1

#выполняется до тех пор пока дрон не приблизится на оптимальное расстояние
#или пока не будет выполнено n шагов (сделано для тестирования алгоритма)
while sqrt((xh - xw) ** 2 + (yh - yw) ** 2 + (oz - zw) ** 2) > r and k < 40:

    # вычисление угла между дроном и целью согласно представленным в отчете формулам
    fiw = atan((xh - xw) / (yh - yw)) + pi * (yw > yh)
    fiwz = atan((oz - zw) / (yh - yw)) + pi * (yw > yh)

    #криволинейное движение
    #xh = xh + vh * t * sin(fih)
    #yh = yh + vh * t * cos(fih)

    #движение в случайном направлении
    xh += random.uniform(A, B)
    yh += random.uniform(A, B)

    xw = xw + vw * t * sin(fiw)
    yw = yw + vw * t * cos(fiw)

    zw = zw + vz * t * sin(fiwz)


    k += 1
    print(xh, yh, xw, yw)

    #для построения графиков в матплот
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

exit(0)